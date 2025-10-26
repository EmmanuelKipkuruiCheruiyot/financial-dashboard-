# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from datetime import datetime, timedelta

app = FastAPI(title="Finsight ERP API")

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] for production security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Core Financial Modules
# ==========================================================

@app.get("/api/revenue-tracking")
def revenue_tracking() -> List[Dict]:
    return [
        {"month": "Jan", "amount": 12000},
        {"month": "Feb", "amount": 15000},
        {"month": "Mar", "amount": 17000},
        {"month": "Apr", "amount": 14000},
        {"month": "May", "amount": 18000},
        {"month": "Jun", "amount": 20000},
        {"month": "Jul", "amount": 19500},
        {"month": "Aug", "amount": 21000}
    ]

@app.get("/api/expenses-management")
def expenses_management() -> List[Dict]:
    return [
        {"category": "Salaries", "value": 5000},
        {"category": "Rent", "value": 2000},
        {"category": "Utilities", "value": 800},
        {"category": "Marketing", "value": 1500},
        {"category": "Office Supplies", "value": 400},
        {"category": "Maintenance", "value": 600},
        {"category": "Misc", "value": 700}
    ]

@app.get("/api/profit-loss")
def profit_loss() -> List[Dict]:
    return [
        {"month": "Jan", "profit": 7000},
        {"month": "Feb", "profit": 9000},
        {"month": "Mar", "profit": 9500},
        {"month": "Apr", "profit": 8200},
        {"month": "May", "profit": 11500},
        {"month": "Jun", "profit": 13000},
        {"month": "Jul", "profit": 12500},
        {"month": "Aug", "profit": 14500}
    ]

@app.get("/api/cash-flow")
def cash_flow() -> List[Dict]:
    return [
        {"month": "Jan", "inflow": 12000, "outflow": 5000},
        {"month": "Feb", "inflow": 15000, "outflow": 6000},
        {"month": "Mar", "inflow": 17000, "outflow": 7000},
        {"month": "Apr", "inflow": 14000, "outflow": 5800},
        {"month": "May", "inflow": 18000, "outflow": 6500},
        {"month": "Jun", "inflow": 20000, "outflow": 7000}
    ]

@app.get("/api/budgeting-forecasting")
def budgeting_forecasting() -> List[Dict]:
    return [
        {"month": "Jan", "budget": 14000, "actual": 12000},
        {"month": "Feb", "budget": 15000, "actual": 15000},
        {"month": "Mar", "budget": 16000, "actual": 17000},
        {"month": "Apr", "budget": 15500, "actual": 14000}
    ]

# ==========================================================
# Operational / Business Modules
# ==========================================================

@app.get("/api/inventory")
def inventory() -> List[Dict]:
    return [
        {"name": "Item A", "stock": 120, "reorder_level": 50},
        {"name": "Item B", "stock": 80, "reorder_level": 30},
        {"name": "Item C", "stock": 40, "reorder_level": 20},
        {"name": "Item D", "stock": 200, "reorder_level": 100}
    ]

@app.get("/api/sales-orders")
def sales_orders() -> List[Dict]:
    return [
        {"order_id": "SO001", "customer": "Alice", "amount": 500, "status": "Delivered"},
        {"order_id": "SO002", "customer": "Bob", "amount": 300, "status": "Pending"},
        {"order_id": "SO003", "customer": "Charlie", "amount": 450, "status": "Delivered"},
        {"order_id": "SO004", "customer": "Diana", "amount": 700, "status": "Processing"}
    ]

@app.get("/api/purchasing")
def purchasing() -> List[Dict]:
    return [
        {"po_id": "PO001", "vendor": "Vendor A", "amount": 1000, "status": "Received"},
        {"po_id": "PO002", "vendor": "Vendor B", "amount": 750, "status": "Ordered"},
        {"po_id": "PO003", "vendor": "Vendor C", "amount": 1200, "status": "Shipped"}
    ]

@app.get("/api/hr")
def hr() -> List[Dict]:
    return [
        {"employee": "John Doe", "role": "Accountant", "status": "Active"},
        {"employee": "Jane Smith", "role": "Manager", "status": "Active"},
        {"employee": "Paul White", "role": "Sales Rep", "status": "On Leave"}
    ]

@app.get("/api/project-management")
def project_management() -> List[Dict]:
    return [
        {"project": "Website Redesign", "status": "Ongoing"},
        {"project": "New CRM Setup", "status": "Planned"},
        {"project": "ERP System Upgrade", "status": "Completed"}
    ]

# ==========================================================
# Analytical / Reporting Modules
# ==========================================================

@app.get("/api/dashboard-kpis")
def dashboard_kpis() -> Dict:
    return {
        "total_revenue": 120000,
        "total_expenses": 48000,
        "profit": 72000,
        "cash_balance": 50000,
        "active_projects": 3
    }

@app.get("/api/financial-ratios")
def financial_ratios() -> Dict:
    return {
        "current_ratio": 1.5,
        "debt_equity_ratio": 0.8,
        "profit_margin": 0.25,
        "return_on_assets": 0.12
    }

@app.get("/api/trend-analysis")
def trend_analysis() -> List[Dict]:
    return [
        {"period": "Q1", "value": 30000},
        {"period": "Q2", "value": 35000},
        {"period": "Q3", "value": 40000},
        {"period": "Q4", "value": 45000}
    ]

@app.get("/api/alerts")
def alerts() -> List[Dict]:
    today = datetime.now()
    return [
        {
            "message": "Inventory of Item B below reorder level",
            "module": "Inventory",
            "severity": "high",
            "date": (today - timedelta(days=1)).strftime("%Y-%m-%d"),
            "suggestion": "Order 50 more units to restock."
        },
        {
            "message": "Profit margin dropped below 20% last month",
            "module": "Finance",
            "severity": "medium",
            "date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
            "suggestion": "Review pricing strategy or cut unnecessary expenses."
        },
        {
            "message": "Upcoming payroll processing deadline in 3 days",
            "module": "HR",
            "severity": "low",
            "date": today.strftime("%Y-%m-%d"),
            "suggestion": "Ensure all salary approvals are completed."
        },
        {
            "message": "New supplier contract requires compliance review",
            "module": "Compliance",
            "severity": "medium",
            "date": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
            "suggestion": "Legal team should review contract terms."
        },
        {
            "message": "Unusual spike in utility expenses detected",
            "module": "Expenses",
            "severity": "high",
            "date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "suggestion": "Investigate possible billing errors or wastage."
        }
    ]

# ==========================================================
# Optional Advanced Modules
# ==========================================================

@app.get("/api/crm")
def crm() -> List[Dict]:
    return [
        {"customer": "Alice", "engagement_score": 80},
        {"customer": "Bob", "engagement_score": 60},
        {"customer": "Charlie", "engagement_score": 75}
    ]

@app.get("/api/supplier-portal")
def supplier_portal() -> List[Dict]:
    return [
        {"supplier": "Vendor A", "open_orders": 5},
        {"supplier": "Vendor B", "open_orders": 2},
        {"supplier": "Vendor C", "open_orders": 4}
    ]

@app.get("/api/audit-compliance")
def audit_compliance() -> List[Dict]:
    return [
        {"audit": "Q1 Financials", "status": "Completed"},
        {"audit": "Payroll Audit", "status": "Pending"},
        {"audit": "Tax Compliance", "status": "Ongoing"}
    ]

# ==========================================================
# Default Fallback
# ==========================================================

@app.get("/api/{module_name}")
def default_module(module_name: str):
    return [
        {"Item": "Example 1", "Value": 100},
        {"Item": "Example 2", "Value": 200}
    ]
