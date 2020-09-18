import React, { useEffect, useState } from 'react';
//import axios from 'axios';

export const Chart = (props) => {

    const APIDjango = "http://127.0.0.1:8000/general/" // Django api
    const [djangoApi, SetApi] = useState([]);

    const FetchData = async () => {
        await fetch(APIDjango)
            .then(response => response.json())
            .then(response => SetApi(response.data))
    };
    
    useEffect(() => {
        FetchData();
    }, []);


    //console.log(djangoApi);

    return (
        <div>
            <div className="container p-4">
                <table className="table table-hover table-sm">
                    <thead className= "thead-dark">
                        <tr>
                            <th scope="col">Country</th>
                            <th scope="col">Casos en total </th>
                            <th scope="col">Actions </th>
                        </tr>
                    </thead>
                    <tbody>
                            {
                                djangoApi.map((element, id) => (
                                    <tr key={id}>
                                        
                                        <th scope="row">{element.country}</th>
                                        <td>{element.casos}</td>
                                        <td>
                                            <a href="#" className = "btn btn-info">Visualizar</a>
                                        </td>
                                       
                                    </tr>
                                ))
                            }
                    </tbody>

                </table>
            </div>
        </div>
    );
};