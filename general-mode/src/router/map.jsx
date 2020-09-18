import React from 'react';
import { Chart } from 'react-google-charts';
import './map.css'

export const Map = () => {
    /*const MapUrl = `https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token=pk.eyJ1IjoicGF5bG9hZDA5MTEiLCJhIjoiY2tmOGtmY2NmMDA2MzJ6bHlzanoybXMzNSJ9.X8l8mU1QNT6VBD08NaW-rw`;

    const Preload = () => {
        const maping = ''; //= loadImage(MapUrl);
        return maping;
    }*/

    return (
        <div>
            <div id="Map">
                <div className= "container p-4" style={{ display: 'flex',  Width: '100%' }}>
                    <Chart
                        width={'1200px'}
                        height={'500px'}
                        chartType="GeoChart"
                        data={[
                            ['Country', 'Infected'],
                            ['Germany', 200],
                            ['United States', 300],
                            ['Brazil', 400],
                            ['Canada', 500],
                            ['France', 600],
                            ['Ecuador', 200000],
                            ['Peru', 200000],
                            ['RU', 700],
                        ]}
                        // Note: you will need to get a mapsApiKey for your project.
                        // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
                        mapsApiKey="YOUR_KEY_HERE"
                        rootProps={{ 'data-testid': '1' }}
                    />
                </div>
            </div>
            {/*<div className="row">
                <div className="col-md-4">
                    <div className="container p-4">
                        <div className="card">
                            <div className="card-body">
                                <div style={{ display: 'flex', position: 'absolute', Width: '100%' }}>
                                    <Chart
                                        width={'200'}
                                        height={'300px'}
                                        chartType="GeoChart"
                                        data={[
                                            ['Country', 'Infected'],
                                            ['Germany', 200],
                                            ['United States', 300],
                                            ['Brazil', 400],
                                            ['Canada', 500],
                                            ['France', 600],
                                            ['Ecuador', 200000],
                                            ['Peru', 200000],
                                            ['RU', 700],
                                        ]}
                                        // Note: you will need to get a mapsApiKey for your project.
                                        // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
                                        mapsApiKey="YOUR_KEY_HERE"
                                        rootProps={{ 'data-testid': '1' }}
                                    />
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>*/}
        </div>
    )
};