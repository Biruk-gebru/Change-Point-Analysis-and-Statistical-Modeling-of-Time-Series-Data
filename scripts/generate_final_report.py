
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
import os
import pandas as pd

# Report Configuration
REPORT_FILENAME = "/home/karanos/kiam/week11/prod/docs/Final_Report_Birhan_Energies.pdf"
AUTHOR = "Biruk Gebru Jember"
TITLE = "Analyzing Brent Oil Price Volatility: Geopolitical Shocks and Regime Shifts"

# Data Paths
BASE_DIR = "/home/karanos/kiam/week11/prod"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
EVENTS_CSV = os.path.join(BASE_DIR, "data/events/geopolitical_events.csv")
IMPACT_CSV = os.path.join(RESULTS_DIR, "statistics/stat_change_point_impact.csv")

def add_image(story, filename, caption, styles, width=450, height=None):
    img_path = os.path.join(FIGURES_DIR, filename)
    if not height:
        height = width * 0.6  # Default aspect ratio if not specified
    
    if os.path.exists(img_path):
        try:
            img = Image(img_path, width=width, height=height)
            story.append(Spacer(1, 10))
            story.append(img)
            story.append(Paragraph(f"<i>{caption}</i>", styles['Caption']))
            story.append(Spacer(1, 10))
        except Exception as e:
            story.append(Paragraph(f"[Image error: {filename} - {str(e)}]", styles['Normal']))
    else:
        story.append(Paragraph(f"[Image not found: {filename}]", styles['Normal']))

def create_report():
    os.makedirs(os.path.dirname(REPORT_FILENAME), exist_ok=True)
    doc = SimpleDocTemplate(REPORT_FILENAME, pagesize=letter,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50) 
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', parent=styles['Normal'], alignment=TA_JUSTIFY, spaceAfter=8, leading=12))
    styles.add(ParagraphStyle(name='ExecutiveSummary', parent=styles['Normal'], alignment=TA_JUSTIFY, spaceAfter=12, leading=14, fontName='Helvetica-Oblique', fontSize=10, leftIndent=20, rightIndent=20))
    styles.add(ParagraphStyle(name='SectionHeader', parent=styles['Heading2'], spaceAfter=8, spaceBefore=12, textColor=colors.darkblue, fontSize=14))
    styles.add(ParagraphStyle(name='SubSectionHeader', parent=styles['Heading3'], spaceAfter=6, spaceBefore=10, fontSize=12))
    styles.add(ParagraphStyle(name='Caption', parent=styles['Italic'], alignment=TA_CENTER, fontSize=8, spaceAfter=8, textColor=colors.grey))
    
    Story = []

    # --- Title ---
    Story.append(Paragraph(TITLE, styles['Heading1']))
    Story.append(Paragraph(f"<b>Birhan Energies Consultancy</b> | <b>Senior Analyst:</b> {AUTHOR}", styles['Normal']))
    Story.append(Spacer(1, 15))

    # --- Executive Summary ---
    Story.append(Paragraph("Executive Summary", styles['SectionHeader']))
    exec_summary = """
    This report presents a comprehensive analysis of Brent oil price dynamics through the lens of Bayesian change point detection. 
    Birhan Energies identifies a critical market regime shift in early 2019, highly correlated with the termination of US sanctions waivers on Iranian oil. 
    Our findings indicate a structural 127% increase in daily price volatility following this event, signaling a transition from supply-driven stability 
    to geopolitically-dominated volatility. For investors and policymakers, these results underscore the necessity of adaptive risk management 
    strategies that account for sudden 'regime shifts' rather than assuming linear price behaviors.
    """
    Story.append(Paragraph(exec_summary, styles['ExecutiveSummary']))

    # --- 1. Business Objective ---
    Story.append(Paragraph("1. Understanding the Business Objective", styles['SectionHeader']))
    objective_text = """
    At Birhan Energies, we recognize that the global energy market is no longer governed solely by supply and demand fundamentals. 
    Geopolitical conflicts, OPEC+ policy pivots, and international sanctions now serve as primary drivers of structural breaks in oil prices. 
    The challenge lies in distinguishing transient market noise from these structural "change points" that redefine market behavior for years. 
    Providing actionable insights for <b>Investors</b> (hedging strategies), <b>Policymakers</b> (energy security), and <b>Energy Companies</b> 
    (operational planning) is the core objective of this project.
    """
    Story.append(Paragraph(objective_text, styles['Justify']))

    # --- 2. Methodology and Completed Work ---
    Story.append(Paragraph("2. Methodology and Data Analysis", styles['SectionHeader']))
    
    Story.append(Paragraph("2.1 Data Foundation (Task 1)", styles['SubSectionHeader']))
    foundation_text = """
    The analysis utilized daily Brent crude price data from 1987 to 2022. Preliminary testing confirmed that raw prices are non-stationary, 
    necessitating a transformation into Log Returns to stabilize mean and variance for robust modeling. We compiled a timeline of 15 key 
    geopolitical events—ranging from the Libyan Civil War to the Russia-Ukraine conflict—to act as historical benchmarks for our statistical findings.
    """
    Story.append(Paragraph(foundation_text, styles['Justify']))

    add_image(Story, "fig_brent_prices_full.png", "Figure 1: Full Historical Brent Crude Prices (1987-2022).", styles, height=150)

    Story.append(Paragraph("2.2 Bayesian Change Point Analysis (Task 2)", styles['SubSectionHeader']))
    modeling_text = """
    We deployed a Bayesian Change Point model using the <b>PyMC</b> framework. Unlike traditional frequentist breaks, our model estimates the 
    joint posterior distribution of a 'switch point' ($\tau$) and the market parameters (mean $\mu$, volatility $\sigma$) before and after the shift. 
    This allows us to quantify the uncertainty of when the market regime actually changed. No-U-Turn Sampling (NUTS) was utilized to achieve 
    reliable convergence, verified via trace plots and R-hat statistics near 1.0.
    """
    Story.append(Paragraph(modeling_text, styles['Justify']))

    add_image(Story, "fig_tau_posterior.png", "Figure 2: Posterior distribution of the detected Change Point ($\tau$).", styles, height=150)
    add_image(Story, "fig_trace_plots.png", "Figure 3: MCMC Trace plots showing model convergence.", styles, height=200)

    # --- 3. Findings: Event Association & Impact ---
    Story.append(PageBreak())
    Story.append(Paragraph("3. Event Association and Impact Quantification", styles['SectionHeader']))
    
    findings_text = """
    The model identified a definitive structural break around <b>November 2018 - May 2019</b>. This period corresponds directly to the 
    <b>US termination of Iran oil sanctions waivers</b>. The market effectively 're-priced' its risk profile in anticipation of the supply squeeze.
    """
    Story.append(Paragraph(findings_text, styles['Justify']))

    # Impact Statistics Table
    if os.path.exists(IMPACT_CSV):
        impact_df = pd.read_csv(IMPACT_CSV)
        table_data = [["Metric", "Value"]] + impact_df.values.tolist()
        t = Table(table_data, colWidths=[180, 180])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.darkblue),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0,0), (-1,0), 12),
                               ('GRID', (0,0), (-1,-1), 1, colors.grey)]))
        Story.append(t)
        Story.append(Spacer(1, 10))

    impact_quant = """
    <b>Quantitative Summary:</b> Following the change point, daily price volatility surged by <b>127.58%</b> (from 0.019 to 0.043). 
    While the mean return remained relatively stable, the distribution centers widened significantly, indicating a 'High Volatility' regime 
    where price swings became more frequent and extreme.
    """
    Story.append(Paragraph(impact_quant, styles['Justify']))

    add_image(Story, "fig_changepoint_on_prices.png", "Figure 4: Detected Regime Shift overlaid on recent Oil Price data.", styles, height=180)

    # --- 4. Interactive Dashboard ---
    Story.append(Paragraph("4. Interactive Dashboard Delivery", styles['SectionHeader']))
    dashboard_text = """
    To empower stakeholders, we developed a full-stack dashboard. The <b>Flask API</b> serves live model summaries and pricing data, 
    while the <b>React Frontend</b> provides an interactive 'Regime Explorer' where analysts can overlay events on price trends and 
    filter by date ranges (1Y, 5Y, All).
    """
    Story.append(Paragraph(dashboard_text, styles['Justify']))

    add_image(Story, "birhanDash.png", "Figure 5: Birhan Energies Client Dashboard - Interactive Regime Analysis.", styles, height=220)

    # --- 5. Strategic Recommendations ---
    Story.append(Paragraph("5. Strategic Recommendations", styles['SectionHeader']))
    
    recom_investors = """
    <b>For Investors:</b> Transition from linear volatility models to regime-switching frameworks. The 2019 shock demonstrates 
    that diversification across asset classes is insufficient during regime shifts; dynamic hedging based on 'Birhan Triggers' is required.
    """
    Story.append(Paragraph(recom_investors, styles['Justify']))

    recom_policy = """
    <b>For Policymakers:</b> Energy security strategies must prioritize supply chain redundancy. The 127% volatility increase 
    suggests that relying on single-source suppliers during 'Sanction Regimes' creates unsustainable economic tail-risks.
    """
    Story.append(Paragraph(recom_policy, styles['Justify']))

    recom_energy = """
    <b>For Energy Companies:</b> Operations should shift toward flexible inventory management. Operational planning must account 
    for wider price corridors, as the 'New Normal' entails structural instability rather than mean-reverting behavior.
    """
    Story.append(Paragraph(recom_energy, styles['Justify']))

    # --- 6. Limitations and Future Work ---
    Story.append(Paragraph("6. Limitations and Future Work", styles['SectionHeader']))
    limitations = """
    <b>Correlation vs. Causation:</b> Statistical change points indicate when a market shift was priced in, but 
    cannot prove single-variable causation. Multiple factors (USD strength, demand shifts) often converge. 
    <b>Model Scope:</b> The current single change point model accurately identifies the <i>most</i> significant break, but energy markets 
    often contain multiple smaller breaks.
    """
    Story.append(Paragraph(limitations, styles['Justify']))

    future_work = """
    <b>Future Roadmap:</b> (1) <b>Multiple Change Points:</b> Extending the model to detect 3-5 structural breaks simultaneously; 
    (2) <b>Advanced Macro Data:</b> Incorporating GDP growth and exchange rates as covariates; (3) <b>Real-time Forecasting:</b> 
    Integrating Markov-Switching models to predict the <i>probability</i> of entering a new high-volatility regime in real-time.
    """
    Story.append(Paragraph(future_work, styles['Justify']))

    doc.build(Story)
    print(f"Final Report generated: {REPORT_FILENAME}")

if __name__ == "__main__":
    create_report()
