const lanIP = `${window.location.hostname}:5000`;
console.log(lanIP)
const socket = io(`http://${lanIP}`);

var prev_switch_status = 0;
var cap_count = 0;
var water_drank_today = 0;

//#region ***  Callback-Visualisation - show___ ***
const show_temperature = (json) => {
    const $temp = document.querySelector(".js-temp");
    // console.log(json);
    console.log(`Water temp: ${json.SensorValue}`);
    $temp.textContent = json.SensorValue;
};

const show_bottlecap_count = (json) => {
    const $bottlecap = document.querySelector(".js-bottlecap");
    console.log(`Bottlecap status: ${json.BottleCapCount}`);
    let cap_count = json.BottleCapCount;
    $bottlecap.textContent = cap_count;
};

const show_daily_waterconsumption = (json) => {
  const $daily_waterconsumption = document.querySelector(".js-goal_waterconsumption");
  $daily_waterconsumption.textContent = `Goal: ${parseFloat(json.WaterConsumptionPerDay / 1000)} liters`;
};

const show_water_percentage = (json) => {
  console.log(json.WaterConsumptionPerDay)
  console.log(json.WaterLoss)
  // waterconsumption_goal = 100%
  const waterconsumption_goal = json.WaterConsumptionPerDay;
  for (const add_water of json.WaterLoss) {
    if (json.WaterLoss == NaN || json.WaterLoss == undefined) {
      water_drank_today = 0;
    } else {
      water_drank_today += add_water;
    }
  }
  
  console.log(`water amount drank today ${water_drank_today}`);

  water_percentage = (water_drank_today / waterconsumption_goal) * 100;
  if (water_percentage >= 100) {
    water_percentage = 100;
  }
  console.log(`Percentage of water drank today ${water_percentage}%`);
  
        //Waterconsumption bar
        var options = {
            series: [water_percentage],
            chart: {
            height: 350,
            type: 'radialBar',
            toolbar: {
              show: false
            }
            },
            plotOptions: {
                radialBar: {
                startAngle: 0,
                endAngle: 360,
                hollow: {
                    margin: 0,
                    size: '70%',
                    background: '#211a45',
                    image: undefined,
                    imageOffsetX: 0,
                    imageOffsetY: 0,
                    position: 'front',
                    dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                    }
                },
                track: {
                    background: '#4e4e4e',
                    strokeWidth: '67%',
                    margin: 0, // margin is in pixels
                    dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                    }
                },
            
                dataLabels: {
                    show: true,
                    name: {
                    offsetY: -10,
                    show: true,
                    color: '#2ee7a2',
                    fontFamily: 'Roboto mono',
                    fontSize: '17px'
                    },
                    value: {
                    formatter: function(val) {
                        return parseInt(val);
                    },
                    color: '#2ee7a2',
                    fontFamily: 'Roboto mono',
                    fontSize: '36px',
                    show: true,
                    }
                }
                }
            },
            fill: {
                type: 'gradient',
                gradient: {
                shade: 'dark',
                type: 'horizontal',
                shadeIntensity: 0.5,
                gradientToColors: ['#fd894f'],
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 100]
                }
            },
            stroke: {
                lineCap: 'round'
            },
            labels: ['Percent'],
            };
  
        var chart_dashboard = new ApexCharts(document.querySelector("#chart__dashboard"), options);
        chart_dashboard.render();
};

const show_history = (json) => {
  console.log(json.WaterLoss);
  // history chart
        var options = {
            series: [{
            name: 'Daily waterconsumption',
            data: json.WaterLoss,
          }],
            chart: {
            height: 350,
            foreColor: '#fff7ff',
            type: 'area',
            color: "#fff7ff",
            fontFamily: 'Roboto mono',
            toolbar: {
                show: false
            }
          },
          fill: {
            colors: "#fd894f"
          },
          markers: {
            colors: '#1d94ff'
         },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            curve: 'smooth',
          },
          xaxis: {
            type: 'datetime',
            categories: json.Date
          },
          tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
          },
          };
  
        var chart_history = new ApexCharts(document.querySelector("#chart__history"), options);
        chart_history.render();
};

//#region ***  Event Listeners - listenTo___ ***
const listenToSocket_dasboard = () => {

  socket.on("connected", () => {
    console.log("verbonden met socket webserver");
  });

  socket.on("b2f_connected", (msg) => {
    console.log(`Eerste boodschap server: huidig aantal ml gedronken in DB ${msg} ml`);
  });

  socket.on("b2f_show_temperature", (json) => {
    console.log(`Temperature caught by front: ${json}`);
    show_temperature(json);
  });

  socket.on("b2f_show_bottlecap", (json) => {
    console.log(`Bottlecap count caught by front: ${json}`);
    show_bottlecap_count(json);
  });

  socket.on("b2f_show_waterconsumption", (json) => {
    console.log(`Waterconsumption_goal caught by front: ${json}`);
    show_daily_waterconsumption(json);
  });

  socket.on("b2f_show_water_percentage", (json) => {
    console.log(`water percentage caught by front: ${json}`);
    show_water_percentage(json);
  });
};

const listenToSocket_history = () => {

  socket.on("connected", () => {
    console.log("verbonden met socket webserver");
  });

  socket.on("b2f_show_daily_waterconsumption_history", (json) => {
    console.log(`water percentage caught by front: ${json}`);
    show_history(json);
  });
};

const listenToUI_dasboard = () => {
  socket.emit("f2b_get_waterconsumption_goal", {person_id: 1});
  socket.emit("f2b_get_water_percentage", {person_id: 1});
  socket.emit("f2b_get_oled_display", {person_id: 1});
  const $add_water_input = document.querySelector(".js-add__water");
  const $add_water_button = document.querySelector(".js-submit__water");

  $add_water_button.addEventListener("click", () => {
    const input_value = $add_water_input.value;
    console.log(`value van input: ${input_value}`);
    socket.emit("f2b_add_water", {water_consumption: input_value});
  });
};

const listenToUI_history = () => {
  socket.emit("f2b_get_daily_water_history", {water_id: 1});
};

const listenToUI_features = () => {
  const $button = document.querySelector(".js-button");
  $button.addEventListener("click", () => {
    let new_status;
    if ($button.dataset.statusbuzzer == 0) {
      new_status = 1;
    } else {
      new_status = 0;
    }
    socket.emit("f2b_toggle_alarm", {buzzer_id: 5, new_status: new_status });
  });
  const $waterconsumption_goal_input = document.querySelector(".js-change__waterconsumption--input");
  const $waterconsumption_goal_button = document.querySelector(".js-change__waterconsumption--button");
  
  $waterconsumption_goal_button.addEventListener("click", () => {
    const input_value = $waterconsumption_goal_input.value;
    console.log(`value van input: ${input_value}`);
    socket.emit("f2b_send_change_waterconsumption", {person_id: 1, water_consumption_goal: input_value});
  });

  $shutdown_button = document.querySelector(".js-shutdown");
  $shutdown_button.addEventListener("click", () => {
    socket.emit("f2b_turn_off_hydrobottle");
  });
};


document.addEventListener("DOMContentLoaded", () => {
  console.info("DOM geladen");
});


//#region ***  INIT / DOMContentLoaded  ***
const init = () => {
    $html_dashboard = document.querySelector(".js-dashboard");
    $html_history = document.querySelector(".js-history");
    $html_features = document.querySelector(".js-features");

    if($html_dashboard) {
      listenToSocket_dasboard();
      listenToUI_dasboard();
    }

    if($html_history) {
      listenToSocket_history();
      listenToUI_history();
    }

    if($html_features) {
      listenToUI_features();
    }
};

document.addEventListener("DOMContentLoaded", init);