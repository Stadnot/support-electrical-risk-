# Support Electrical Risk


## Problema Statement
Los empresas distribuidoras de energía eléctrica enfrentan diversos problemas con las interrupciones eléctricas. Esto se traduce en un riesgo para la satisfacción del cliente, aumento de costos operacionales y menores ventas a clientes libres.
Actualmente las soluciones se ejecutan de forma reactiva y la disponibilidad de técnicos varía respecto a las interrupciones generadas que se traducen en restricciones para la atención de los siniestros.

Este proyecto busca contruir un **sistema de puntaje de riesgo** que predice qué alimentadores eléctricos tienen más probabilidad de presentar fallos severos durante los próximos 7 días habilitando la toma decisiones de mantenimiento proactivo.

## Severity Definition
Una interrupción es clasificado como severa basado en la regulación de consesiones por parte de la Ley de conseciones eléctricas.

| Zone | Max duration | Customers affected |
|------|-------------|-------------------|
| Metropolitano | > 300 min | >= 1 |
| Extended | > 700 min | >= 1 |

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
