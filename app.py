from flask import Flask, render_template, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

class ResoDataService:
    def __init__(self):
        self.data = None
        self.last_fetch = None
        
    def fetch_data(self):
        try:
            response = requests.get('https://services.reso.org/orgs')
            response.raise_for_status()
            self.data = response.json()
            self.last_fetch = datetime.now()
            return True
        except Exception as e:
            print(f"Error fetching data: {e}")
            return False
    
    def get_organizations(self):
        if not self.data:
            self.fetch_data()
        return self.data.get('Organizations', [])
    
    def search_organizations(self, query="", org_type="", state="", country=""):
        orgs = self.get_organizations()
        
        if not orgs:
            return []
            
        results = []
        query = query.lower() if query else ""
        
        for org in orgs:
            if query and query not in org.get('OrganizationName', '').lower():
                continue
                
            if org_type and org.get('OrganizationType') != org_type:
                continue
                
            if state and org.get('OrganizationStateOrProvince') != state:
                continue
                
            if country and org.get('OrganizationCountry') != country:
                continue
                
            results.append(org)
            
        return results

data_service = ResoDataService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/organizations')
def get_organizations():
    query = request.args.get('query', '')
    org_type = request.args.get('type', '')
    state = request.args.get('state', '')
    country = request.args.get('country', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    
    results = data_service.search_organizations(query, org_type, state, country)
    total_count = len(results)
    
    # Calculate pagination
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_results = results[start_idx:end_idx]
    
    total_pages = (total_count + per_page - 1) // per_page
    
    return jsonify({
        'organizations': paginated_results,
        'count': len(paginated_results),
        'total_count': total_count,
        'page': page,
        'per_page': per_page,
        'total_pages': total_pages,
        'has_next': page < total_pages,
        'has_prev': page > 1,
        'last_updated': data_service.last_fetch.isoformat() if data_service.last_fetch else None
    })

@app.route('/api/stats')
def get_stats():
    orgs = data_service.get_organizations()
    
    if not orgs:
        return jsonify({'error': 'No data available'})
    
    stats = {
        'total_organizations': len(orgs),
        'types': {},
        'states': {},
        'countries': {}
    }
    
    for org in orgs:
        org_type = org.get('OrganizationType') or 'Unknown'
        state = org.get('OrganizationStateOrProvince') or 'Unknown'
        country = org.get('OrganizationCountry') or 'Unknown'
        
        stats['types'][org_type] = stats['types'].get(org_type, 0) + 1
        stats['states'][state] = stats['states'].get(state, 0) + 1
        stats['countries'][country] = stats['countries'].get(country, 0) + 1
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7766, debug=True)