import React, {useEffect, useState} from 'react';
import { Chart } from 'react-google-charts';
import './map.css'

export const Map = () => {

    const DjangoAPI = `http://127.0.0.1:8000/general/global/`;
    const [country, SetCountry] = useState([]);
    //  const AsigData = {};


    /*const MapUrl = `https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token=pk.eyJ1IjoicGF5bG9hZDA5MTEiLCJhIjoiY2tmOGtmY2NmMDA2MzJ6bHlzanoybXMzNSJ9.X8l8mU1QNT6VBD08NaW-rw`;

    const Preload = () => {
        const maping = ''; //= loadImage(MapUrl);
        return maping;
    }*/

    useEffect(()=>{
        fetch(DjangoAPI)
            .then(response => response.json())
            .then(response => SetCountry(response.data))
            .catch(err => console.log(err))
    },[]);


    //console.log(typeof(country));
    const values_ = [['Country', 'Infected']];
    // ['Country', 'Infected'],

    //console.log(country.length);

    for (let i= 0; i < country.length; i++){
        //console.log(country[i]);
        if (country[i][0] == "United States of America" ){
            values_.push(['United States',country[i][1]])
        }else if(country[i][0] == "Russian Federation"){
            values_.push(['RU',country[i][1]])
        }
        else if(country[i][0] == "Bolivia (Plurinational State of)"){
            values_.push(['Bolivia',country[i][1]])
        }
        else if(country[i][0] == "Iran (Islamic Republic of)"){
            values_.push(['Iran',country[i][1]])
        }
        else if(country[i][0] == "Syrian Arab Republic"){
            values_.push(['Syria',country[i][1]])
        }
        else if(country[i][0] == "The United Kingdom"){
            //alert('congo')
            values_.push(['United Kingdom',country[i][1]])
        }
        else if(country[i][0] == "Congo"){
            //alert('congo')
            values_.push([' Democratic Republic of the Congo',country[i][1]])
        }
        else {
            values_.push(country[i])
        }

        // Syrian Arab Republic United Kingdom
        //Democratic Republic of the Congo
        

    }
    return (
        <div>
            <div id="Map">
                <div className= "container p-4" style={{ display: 'flex',  Width: '100%' }}>
                    <Chart
                        width={'1200px'}
                        height={'500px'}
                        chartType="GeoChart"
                        data={
                            values_
                        }
                        
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