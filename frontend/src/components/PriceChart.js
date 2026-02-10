import React, { useState } from 'react';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
    ReferenceLine
} from 'recharts';

const PriceChart = ({ data, events, changePoint }) => {
    const [timeRange, setTimeRange] = useState('All');

    // Filter data based on selected time range
    const getFilteredData = () => {
        if (!data || data.length === 0) return [];

        // Total data is already filtered/sorted in App or Service
        // We treat the current data as the 'Full' set for the analysis period
        if (timeRange === '1Y') return data.slice(-252);
        if (timeRange === '5Y') return data.slice(-1260);
        return data;
    };

    const filteredData = getFilteredData();

    const CustomTooltip = ({ active, payload, label }) => {
        if (active && payload && payload.length) {
            return (
                <div className="custom-tooltip">
                    <p className="font-semibold text-sm mb-1">{label}</p>
                    <p className="text-cyan-400 text-sm">
                        Price: ${payload[0].value.toFixed(2)}
                    </p>
                </div>
            );
        }
        return null;
    };

    return (
        <div className="w-full">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4">
                <div>
                    <h2 className="text-2xl font-bold text-foreground">Brent Crude Price Analysis</h2>
                    <p className="text-sm text-muted-foreground mt-1">
                        Historical price trends with detected regime shifts and geopolitical events
                    </p>
                </div>
                <div className="flex gap-2 bg-secondary/50 p-1 rounded-lg border border-border">
                    {['1Y', '5Y', 'All'].map((range) => (
                        <button
                            key={range}
                            onClick={() => setTimeRange(range)}
                            className={`px-4 py-1.5 text-xs font-medium rounded-md transition-all ${timeRange === range
                                ? 'bg-primary text-primary-foreground shadow-sm'
                                : 'text-muted-foreground hover:text-foreground'
                                }`}
                        >
                            {range}
                        </button>
                    ))}
                </div>
            </div>

            <ResponsiveContainer width="100%" height={500}>
                <LineChart
                    data={filteredData}
                    margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
                >
                    <CartesianGrid strokeDasharray="3 3" stroke="hsl(240 3.7% 15.9%)" />
                    <XAxis
                        dataKey="Date"
                        stroke="hsl(240 5% 64.9%)"
                        tick={{ fill: 'hsl(240 5% 64.9%)', fontSize: 12 }}
                        tickFormatter={(value) => {
                            const date = new Date(value);
                            return date.getFullYear();
                        }}
                    />
                    <YAxis
                        label={{ value: 'Price (USD)', angle: -90, position: 'insideLeft', fill: 'hsl(240 5% 64.9%)' }}
                        stroke="hsl(240 5% 64.9%)"
                        tick={{ fill: 'hsl(240 5% 64.9%)', fontSize: 12 }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Legend
                        wrapperStyle={{ paddingTop: '20px' }}
                        iconType="line"
                    />

                    {/* Main Price Line */}
                    <Line
                        type="monotone"
                        dataKey="Price"
                        stroke="#22d3ee"
                        strokeWidth={2}
                        dot={false}
                        name="Brent Crude (USD)"
                        animationDuration={1000}
                    />

                    {/* Change Point Reference Line */}
                    {changePoint && changePoint["Change Point Date"] && (
                        <ReferenceLine
                            x={changePoint["Change Point Date"]}
                            stroke="#ef4444"
                            strokeWidth={2}
                            strokeDasharray="5 5"
                            label={{
                                value: 'Regime Shift',
                                position: 'top',
                                fill: '#ef4444',
                                fontSize: 12,
                                fontWeight: 'bold'
                            }}
                        />
                    )}

                    {/* Event Reference Lines (show only major events to avoid clutter) */}
                    {events.slice(0, 6).map((event, index) => (
                        <ReferenceLine
                            key={index}
                            x={event.Date}
                            stroke="#10b981"
                            strokeWidth={1}
                            strokeDasharray="3 3"
                        />
                    ))}
                </LineChart>
            </ResponsiveContainer>

            {/* Change Point Info Card */}
            {changePoint && (
                <div className="mt-6 grid gap-4 md:grid-cols-3">
                    <div className="rounded-lg border border-border bg-secondary p-4">
                        <div className="text-xs text-muted-foreground mb-1">Detected Change Point</div>
                        <div className="text-lg font-bold text-red-400">{changePoint["Change Point Date"]}</div>
                    </div>
                    <div className="rounded-lg border border-border bg-secondary p-4">
                        <div className="text-xs text-muted-foreground mb-1">Volatility Increase</div>
                        <div className="text-lg font-bold text-orange-400">{changePoint["Volatility Change (%)"]}</div>
                    </div>
                    <div className="rounded-lg border border-border bg-secondary p-4">
                        <div className="text-xs text-muted-foreground mb-1">Mean Change</div>
                        <div className="text-lg font-bold text-green-400">{(parseFloat(changePoint["Mean Change"]) * 100).toFixed(3)}%</div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default PriceChart;
