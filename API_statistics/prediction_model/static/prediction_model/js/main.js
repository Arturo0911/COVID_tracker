$(document).ready(function(){

    const Selector = document.getElementById('country_select');
    let datos = [];
    


    Selector.addEventListener('change', ()=>{
        //alert($('#country_select').val())
        console.log(Selector.value);
        /*$.ajax({
            method: 'POST',
            url: `http://127.0.0.1:8000/country/${Selector.value}`,

        })*/
        data  = Selector.value;
        json_value = {
            'country': Selector.value
        }
        new_json = JSON.stringify(json_value)//  we must to parse to json type to send by AJAX
        $.post('http://127.0.0.1:8000/api/',new_json, function(data){
            //console.log(data);
        });
        $.ajax({
            method:"GET",
            url: `http://127.0.0.1:8000/country_reponse/${Selector.value}`,
            success: function(data){
                datos = data;
                console.log(data);
                const ctx = document.getElementById('Mychart').getContext('2d');
                var scatterChart = new Chart(ctx, {
                    type: 'scatter',
                    data: {
                    datasets: [{
                        label: 'Scatter Dataset',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: data['cases']
                        /*data: [{
                            x: 3,
                            y: 5
                        }, {
                            x: 7,
                            y: 8
                        }, {
                            x: 8,
                            y: 8
                        },{
                            x: 9,
                            y: 10
                        },{
                            x: 4,
                            y: 3
                        },{
                            x: 2,
                            y: 2
                        },{
                            x: 5,
                            y: 3
                        },{
                            x: 10,
                            y: 8
                        },{
                            x: 8,
                            y: 9
                        },{
                            x: 7,
                            y: 8
                        }]*/
                    }]
                },
                    options: {
                        scales: {
                            xAxes: [{
                                type: 'linear',
                                position: 'bottom'
                                }]
                            }
                        }
                    });
            }
        });
    

        // =========================================================================================
        // ==============================   CHART JS    ============================================

        
        
    });
    
    
    

});