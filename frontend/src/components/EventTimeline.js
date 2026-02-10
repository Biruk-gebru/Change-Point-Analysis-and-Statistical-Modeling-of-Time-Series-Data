import React from 'react';
import { motion } from 'framer-motion';

const EventTimeline = ({ events, onEventClick }) => {
    const getCategoryColor = (category) => {
        switch (category) {
            case 'Conflict':
                return 'bg-red-500/10 text-red-400 border-red-500/20';
            case 'Sanctions':
                return 'bg-orange-500/10 text-orange-400 border-orange-500/20';
            case 'OPEC Policy':
                return 'bg-blue-500/10 text-blue-400 border-blue-500/20';
            case 'Policy':
                return 'bg-purple-500/10 text-purple-400 border-purple-500/20';
            default:
                return 'bg-gray-500/10 text-gray-400 border-gray-500/20';
        }
    };

    return (
        <div className="h-[calc(100vh-180px)] rounded-lg border border-border bg-card overflow-hidden flex flex-col">
            <div className="sticky top-0 bg-card border-b border-border p-4 z-10">
                <h3 className="font-semibold text-lg">Geopolitical Events</h3>
                <p className="text-xs text-muted-foreground mt-1">{events.length} events tracked</p>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-3">
                {events.map((event, idx) => (
                    <motion.div
                        key={idx}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: idx * 0.05 }}
                        className="group relative rounded-lg border border-border bg-secondary/50 p-3 hover:bg-secondary hover:border-cyan-500/50 cursor-pointer transition-all duration-200"
                        onClick={() => onEventClick && onEventClick(event)}
                    >
                        <div className="flex items-start justify-between gap-2 mb-2">
                            <span className="text-xs font-mono text-cyan-400">
                                {new Date(event.Date).toLocaleDateString('en-US', {
                                    year: 'numeric',
                                    month: 'short',
                                    day: 'numeric'
                                })}
                            </span>
                            <span className={`text-xs px-2 py-0.5 rounded-full border ${getCategoryColor(event.Category)}`}>
                                {event.Category}
                            </span>
                        </div>

                        <h4 className="text-sm font-semibold text-foreground mb-1 line-clamp-2 group-hover:text-cyan-400 transition-colors">
                            {event.Event}
                        </h4>

                        {event.Description && (
                            <p className="text-xs text-muted-foreground line-clamp-2">
                                {event.Description}
                            </p>
                        )}

                        {event.Expected_Impact && (
                            <div className="mt-2 pt-2 border-t border-border/50">
                                <span className="text-xs text-muted-foreground">
                                    Impact: <span className="text-foreground">{event.Expected_Impact}</span>
                                </span>
                            </div>
                        )}
                    </motion.div>
                ))}
            </div>
        </div>
    );
};

export default EventTimeline;
