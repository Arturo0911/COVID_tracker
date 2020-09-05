$(document).ready(function(){

    const Selector = document.getElementById('country_select');
    const Filter = document.getElementById('filter_select');
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
            url: `http://127.0.0.1:8000/country_reponse/${Selector.value}/${Filter.value}`,
            success: function(data){
                //datos = data;
                console.log(data);
                const ctx = document.getElementById('Mychart').getContext('2d');
                var scatterChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                    labels: ['Enero', 'Febrero', 'Marzo'],
                    datasets: [{
                        label: 'Scatter Dataset',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [25,30,66],
                        //data: data['cases'],
                        pointRadius: 0,
                        lineTension: 0,
                        borderWidth: 2,
                        fill: false
                    }]
                },
                    options: {
                        scales: {
                            xAxes: [{
                                type: 'linear',
                                position: 'bottom'
                                }]
                            },
                        animation:{
                            duration:0
                        }
                        }
                    });
            }
        });
    

        // =========================================================================================
        // ==============================   CHART JS    ============================================

        
        
    });
    
    
    

});