from graph import model_trace, trace_rss, pair_colors, plot_side_by_side
from graph import trace_values


m_values = [.5, .6]
b = 100
rss_traces = []
model_traces = []
ad_spends = [800, 1500, 2000, 3500, 4000]
tshirt_sales = [330, 780, 1130, 1310, 1780]

actual_trace = trace_values(x_values = ad_spends, y_values = tshirt_sales)

for m in m_values:
    rss_trace = trace_rss(m, b, ad_spends, tshirt_sales)
    rss_traces.append(rss_trace)
    built_model_trace = model_trace(m, b, ad_spends, tshirt_sales)
    model_traces.append(built_model_trace)
    
pair_colors(model_traces, rss_traces)
figure = plot_side_by_side([actual_trace] + model_traces, rss_traces)