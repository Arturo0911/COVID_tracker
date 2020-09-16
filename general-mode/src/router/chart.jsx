import React, {useEffect, useState} from 'react';
import axios from 'axios';

export const Chart = () => {

    const APIDjango = "http://127.0.0.1:8000/general/" // Django api
    const [djangoApi, SetApi] = useState([]);

    useEffect(()=>{
        axios.get(APIDjango)
            .then(res => {
                //console.log(res);
                SetApi(res.data)
            })
            .catch(err => {
                console.log(err);
            })
    }, []);

    //console.log(djangoApi);
    /*fetch(APIDjango)
        .then((response) => response.json())
        .then((response) => SetApi(response.data))
        .then((response)=> console.log(api));*/

    return (
        <div>
            <ul>
            {djangoApi.map(apis => (
                <li key ={apis.id} >{apis}</li>
                ))}
            </ul>
        </div>
    );
};