# Support Electrical Risk


## Problema Statement
Los empresas distribuidoras de energía eléctrica enfrentan diversos problemas con las interrupciones eléctricas. Esto se traduce en un riesgo para la satisfacción del cliente, aumento de costos operacionales y menores ventas a clientes libres.
Actualmente las soluciones se ejecutan de forma reactiva y la disponibilidad de técnicos varía respecto a las interrupciones generadas que se traducen en restricciones para la atención de los siniestros.

Este proyecto busca contruir un **sistema de puntaje de riesgo** que predice qué alimentadores eléctricos tienen más probabilidad de presentar fallos severos durante los próximos 7 días habilitando la toma decisiones de mantenimiento proactivo.

## Data Processing Decisions

### Duration Calculation
The official column `Duración de incidencia [min]` is used as the primary 
duration source. Records with negative duration values are removed as they 
represent system registration errors.

### Data Quality Filters Applied
| Filter | Records removed | Reason |
|--------|----------------|---------|
| Negative duration | 68 | System registration errors |
| Extreme outliers (> 10,000 min) | 76 | Likely unclosed tickets or system errors |
| **Final dataset** | **227,708** | Ready for analysis |

### Severity Thresholds (based on Ley de Concesiones Eléctricas)
| Zone | Max duration before severe |
|------|---------------------------|
| Metropolitan | > 300 min |
| Extended (Cañete, etc.) | > 700 min |

## Duration Calculation
Para el cáculo de la duración vamos a utilizar: 
- Si `ATR` existe → Duration = ATR - Fecha de interrupción
- Si `ATR` está vacío → Duration = Fecha de Cierre - Fecha de interrupción
- Si ambos están vacíos → NaN (manual review required)

## Scope
- **Voltage level:** Low voltage (BT) only
- **Prediction unit:** Electrical feeder (alimentador)
- **Prediction horizon:** 7 days
- **Data available:** January 2024 - February 2026

## Project Structure
```
support-electrical-risk/
├── data/
│   ├── raw/          # Original data (not uploaded - sensitive)
│   └── processed/    # Cleaned data ready for modeling
├── notebooks/        # Exploratory analysis and modeling
├── src/              # Reusable Python modules
│   └── config.py     # Business rules and parameters
├── app/              # Streamlit dashboard
└── models/           # Trained models
```

## Tech Stack
- Python 3.12
- pandas, scikit-learn, plotly
- Streamlit (dashboard)


## Status
In progress — Phase 1: Exploratory Data Analysis

## Notes on Data Privacy
This project uses proprietary data from Luz del Sur (a Peruvian electric 
distribution company). For confidentiality reasons:
- Raw and processed data are not included in this repository
- Notebooks are excluded as they contain internal system structure
- A synthetic dataset and clean notebooks will be added upon project completion

If you want to reproduce this project, the data pipeline is fully documented
in `src/` and can be adapted to any similar electric utility dataset.