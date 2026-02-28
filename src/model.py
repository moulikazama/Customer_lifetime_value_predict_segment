def calculate_clv(rfm):

    rfm['AOV'] = rfm['Monetary'] / rfm['Frequency']
    rfm['Lifespan_Score'] = 365 - rfm['Recency']

    rfm['CLV'] = rfm['AOV'] * rfm['Frequency'] * (rfm['Lifespan_Score'] / 365)

    return rfm
