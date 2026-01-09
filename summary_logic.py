def generate_ai_case_summary(row):
    case_type = row.get("case_type", "case")
    stage = row.get("remappedstages", "the current stage")
    year = row.get("caseyear", "the relevant year")
    state = row.get("state", "the concerned jurisdiction")
    adjourned = row.get("adjourned", 0)
    hearing_gap = row.get("hearinggap_days", None)
    authority = "Registrar (Judicial)"

    # Safe handling
    try:
        adjourned = int(adjourned)
    except:
        adjourned = 0

    gap_text = (
        f"with a moderate inter-hearing gap of approximately {int(hearing_gap)} days"
        if hearing_gap and hearing_gap == hearing_gap
        else "with no significant inter-hearing gaps recorded"
    )

    adj_text = (
        "and no adjournments recorded in the available hearing history"
        if adjourned == 0
        else f"and {adjourned} adjournment(s) recorded in the available hearing history"
    )

    summary = (
        f"The present {case_type} case, instituted in the year {year} before the courts of {state}, "
        f"is presently listed at the {stage} stage. Based on the available procedural record, "
        f"the matter has come up for hearing once, {gap_text}, {adj_text}. "
        f"The case is currently listed before the {authority}. "
        f"This AI-assisted summary is generated to support judicial review by highlighting "
        f"procedural progression and relevant scheduling considerations."
    )

    return summary
