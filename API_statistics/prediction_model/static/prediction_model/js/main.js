$(document).ready(function () {
  const Selector = document.getElementById("country_select");

  const Filter = document.getElementById("filter_select");
  //let datos = [];

  //const

  Selector.addEventListener("change", () => {
    // Infected chart
    let xMonths = [];
    let yCases = [];

    // Deaths chart

    let xInfected = [];
    let yInfected = [];

    data = Selector.value;
    json_value = {
      country: Selector.value,
    };
    new_json = JSON.stringify(json_value); //  we must to parse to json type to send by AJAX
    $.post("http://127.0.0.1:8000/api/", new_json, function (data) {
      //console.log(data);
    });
    $.ajax({
      method: "GET",
      url: `http://127.0.0.1:8000/country_reponse/${Selector.value}`,
      success: function (data) {
        //datos = data;
        //console.log(data["cases"]);
        data["cases"].forEach((element) => {
          //console.log(element.Mes);
          xMonths.push(element.Mes);
          yCases.push(element.casos);
        });
        console.log(xMonths);
        const ctx = document.getElementById("Mychart").getContext("2d");
        const myChart = new Chart(ctx, {
          type: "line",
          data: {
            labels: xMonths,
            datasets: [
              {
                label: "# Infected by month",
                data: yCases,
                backgroundColor: [
                  "rgba(255, 99, 132, 0.2)",
                  "rgba(54, 162, 235, 0.2)",
                  "rgba(255, 206, 86, 0.2)",
                  "rgba(75, 192, 192, 0.2)",
                  "rgba(153, 102, 255, 0.2)",
                  "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                  "rgba(255, 99, 132, 1)",
                  "rgba(54, 162, 235, 1)",
                  "rgba(255, 206, 86, 1)",
                  "rgba(75, 192, 192, 1)",
                  "rgba(153, 102, 255, 1)",
                  "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              yAxes: [
                {
                  ticks: {
                    beginAtZero: true,
                  },
                },
              ],
            },
          },
        });
      },
    });
    $.ajax({
      method: "GET",
      url: `http://127.0.0.1:8000/death_by_country/${Selector.value}`,
      success: function (values) {
        values["deaths"].forEach((row) => {
          xInfected.push(row.Mes);
          yInfected.push(row.muertes);
        });
        const ctxDeath = document.getElementById("Mychart2").getContext("2d");
        const myChart2 = new Chart(ctxDeath, {
          type: "line",
          data: {
            labels: xInfected,
            datasets: [
              {
                label: "# Death by month",
                data: yInfected,
                backgroundColor: [
                  "rgba(255, 99, 132, 0.2)",
                  "rgba(54, 162, 235, 0.2)",
                  "rgba(255, 206, 86, 0.2)",
                  "rgba(75, 192, 192, 0.2)",
                  "rgba(153, 102, 255, 0.2)",
                  "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                  "rgba(255, 99, 132, 1)",
                  "rgba(54, 162, 235, 1)",
                  "rgba(255, 206, 86, 1)",
                  "rgba(75, 192, 192, 1)",
                  "rgba(153, 102, 255, 1)",
                  "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              yAxes: [
                {
                  ticks: {
                    beginAtZero: true,
                  },
                },
              ],
            },
          },
        });
      },
    });
  });
});
