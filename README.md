# Kartra

Kartra is an all-in-one marketing platform and sales funnel builder. It provides a comprehensive suite of tools for businesses to manage their online presence, market products, generate leads, and automate sales and marketing processes.

## Key Features
- **Page Builder:** Drag-and-drop interface for creating landing pages, sales pages, checkout pages, and more.
- **Email & SMS Marketing:** Automated campaigns with templates, segmentation, behavioral triggers, A/B testing, and analytics.
- **Sales Funnel Builder:** Design and automate multi-step funnels with email sequences, lead tagging, and expert-crafted campaigns.
- **Membership Sites:** Manage programs with tiers, drip content, video hosting, progress tracking, and recurring payments.
- **Video Hosting:** Host marketing and product videos with call-to-action pop-ups, lead tagging, and mobile responsiveness.
- **Lead Management (CRM):** Capture, track, tag, and score leads for personalized marketing.
- **Checkouts:** Secure online sales with customizable pages, one-click upsells/downsells, and abandoned cart recovery.
- **Affiliate Management:** Configure affiliate programs with commission options, payments, tracking, and reporting.
- **Helpdesk:** Ticketing system for customer support with agent assignment, canned responses, and performance tracking.
- **Integrations:** Connect to third-party tools like payment gateways, email services, CRMs, and social platforms.
- **Analytics:** Track campaigns, sales, leads, and other key metrics for optimization.
- **Kartra AI:** Generate marketing copy based on prompts and user data.

## Target Audience
Entrepreneurs, coaches, consultants, marketers, and small to medium-sized businesses looking to build and grow their online presence and digital product businesses. Ideal for those seeking an integrated, all-in-one solution for managing various aspects of their online operations.

## Key Benefits
- **Cost-effectiveness:** Replace multiple specialized tools with a single platform.
- **Time-saving:** Streamline workflows and automate tasks.
- **Simplified management:** Centralized dashboard for business operations.
- **Increased efficiency:** Integrated tools and automations optimize marketing and sales.
- **Scalability:** Pricing plans for different business sizes and growth stages.
- **Beginner-friendly:** User-friendly interface and drag-and-drop editors.

## Potential Limitations
- May not suit large-scale businesses needing highly specialized features.
- Interface may require a learning curve for complete beginners.

## Project Structure
```
src/
  feature_name/
    __init__.py
    feature_name.py
tests/
  feature_name/
    test_feature_name.py
```
Each feature directory represents a core module of the Kartra platform and includes placeholder code and tests.

## Setup
1. Ensure Python 3.11+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest
   ```

## n8n Integration
Kartra can use [n8n](https://n8n.io) for external workflow automation.

### Deploy an n8n Instance
Run a local instance with Docker:
```bash
docker run -it --rm -p 5678:5678 n8nio/n8n
```
Alternatively, sign up for the hosted n8n Cloud service.

### Obtain an API Key
In the n8n dashboard navigate to **Settings → API**, enable the API and copy the generated key.

### Configure Environment Variables
Point the app to your n8n server by setting the following variables:
```bash
export N8N_BASE_URL=http://localhost:5678
export N8N_API_KEY=your-api-key
export N8N_EXAMPLE_WORKFLOW_ID=<workflow-id>
```
Define additional variables for any other workflow IDs your application triggers.

### Trigger Workflows
Use the helper in `src/integrations/n8n_client.py`:
```python
from src.integrations import n8n_client

n8n_client.trigger_workflow(N8N_EXAMPLE_WORKFLOW_ID, {"foo": "bar"})
```
The `requests` dependency required for this integration has been added to `requirements.txt`.

## Contributing
1. Fork the repository and create your branch from `main`.
2. Make changes and add tests where applicable.
3. Ensure `pytest` passes.
4. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the [MIT License](LICENSE).

