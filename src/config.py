# =============================================================
# Business rules and model parameters
# Modify this file when regulatory criteria change
# =============================================================

# Severity thresholds by zone
SEVERITY = {
    "metropolitan": {
        "duration_minutes": 300,
        "customers_affected": 1
    },
    "extended": {
        "duration_minutes": 700,
        "customers_affected": 1
    }
}

# Zones classified as extended (non-metropolitan)
EXTENDED_ZONES = [
    # Add district names here once confirmed
    # Example: "CAÑETE", "MALA", "ASIA"
]

# Prediction horizon in days
PREDICTION_HORIZON_DAYS = 7

# Duration calculation strategy
# "hybrid" = ATR if available, otherwise Fecha de Cierre
DURATION_STRATEGY = "hybrid"

# Voltage level in scope
VOLTAGE_SCOPE = "BT"