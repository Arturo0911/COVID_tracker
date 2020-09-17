import React, { useEffect, useState } from 'react';
//import axios from 'axios';

export const Chart = (props) => {

    //const APIDjango = "http://127.0.0.1:8000/general/" // Django api
    const jsonAPI = "https://jsonplaceholder.typicode.com/posts"; // Json placeholder examples
    const [djangoApi, SetApi] = useState([]);

    const FetchData = async () => {

        await fetch(jsonAPI)
            .then(response => response.json())
            .then(response => SetApi(response))



        /*let r = await fetch(jsonAPI);
        const data = await r.json();
        SetApi(data)*/
    };
    //console.log(typeof(djangoApi));
    //console.log(djangoApi);
    useEffect(() => {
        FetchData();
        /*axios.get(jsonAPI)
            //.then((response)=> response.json())
            .then(res => {SetApi(res.data)})
            .catch(err => console.log(err))*/
    }, []);


    console.log(djangoApi);

    return (
        <div>
            <div className="container p-4">
                <table className="table">
                    <thead>
                        <tr>
                            <th>Id del usuario</th>
                            <th>Id </th>
                            <th> titulo </th>
                            
                        </tr>
                    </thead>
                    <tbody>
                            {
                                djangoApi.map((element, id) => (
                                    <tr key={id}>
                                        <td>{element.userId}</td>
                                        <td>{element.id}</td>
                                        <td>{element.title}</td>
                                    </tr>
                                ))
                            }
                    </tbody>

                </table>
            </div>
        </div>
    );
};