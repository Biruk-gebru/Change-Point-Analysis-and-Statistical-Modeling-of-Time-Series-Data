import React, { useEffect, useState } from 'react';
import './App.css';
import PriceChart from './components/PriceChart';
import EventTimeline from './components/EventTimeline';
import { fetchPrices, fetchEvents, fetchChangePoint } from './services/api';

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoint, setChangePoint] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [pricesData, eventsData, cpData] = await Promise.all([
          fetchPrices(),
          fetchEvents(),
          fetchChangePoint()
        ]);
        setPrices(pricesData);
        setEvents(eventsData);
        setChangePoint(cpData);
      } catch (error) {
        console.error("Failed to load dashboard data:", error);
      } finally {
        setIsLoading(false);
      }
    };
    loadData();
  }, []);

  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 max-w-screen-2xl items-center px-4">
          <div className="mr-4 flex">
            <a className="mr-6 flex items-center space-x-2" href="/">
              <span className="font-bold text-xl bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                Birhan Energies
              </span>
            </a>
          </div>
          <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
            <div className="w-full flex-1 md:w-auto md:flex-none">
              <span className="text-sm text-muted-foreground">Interactive Oil Price Dashboard</span>
            </div>
            <nav className="flex items-center gap-4">
              <div className="flex items-center gap-2">
                <div className={`h-2 w-2 rounded-full ${isLoading ? 'bg-yellow-500 animate-pulse' : 'bg-green-500'}`} />
                <span className="text-xs text-muted-foreground">{isLoading ? 'Syncing...' : 'Live'}</span>
              </div>
            </nav>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container max-w-screen-2xl px-4 py-6">
        <div className="grid gap-6 md:grid-cols-4">
          {/* Main Chart Area - Takes 3 columns */}
          <div className="md:col-span-3 rounded-lg border border-border bg-card p-6">
            {isLoading ? (
              <div className="flex items-center justify-center h-[600px]">
                <div className="flex flex-col items-center gap-4">
                  <div className="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent" />
                  <p className="text-sm text-muted-foreground">Loading market data...</p>
                </div>
              </div>
            ) : (
              <PriceChart
                data={prices}
                events={events}
                changePoint={changePoint}
              />
            )}
          </div>

          {/* Sidebar: Event Timeline - Takes 1 column */}
          <div className="md:col-span-1">
            <EventTimeline events={events} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
