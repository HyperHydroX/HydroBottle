{   
    const init = () => {
        // Navigation mobile
        const $nav_button = document.querySelector(".c-nav__button");
        const $nav_menu = document.querySelector(".c-nav");
        const $nav_link = document.querySelectorAll(".c-nav__link");
        
        // Open & close navigation by pressing the button
        $nav_button.addEventListener("click", () => {
            $nav_button.classList.toggle("open");
            $nav_menu.classList.toggle("active");
        });

        // Close navigation when you click on a link
        $nav_link.forEach(e => e.addEventListener("click", () => {
            $nav_button.classList.remove("open");
            $nav_menu.classList.remove("active");
        }));

        // //Waterconsumption bar
        // var options = {
        //     series: [75],
        //     chart: {
        //     height: 350,
        //     type: 'radialBar',
        //     toolbar: {
        //       show: false
        //     }
        //     },
        //     plotOptions: {
        //         radialBar: {
        //         startAngle: 0,
        //         endAngle: 360,
        //         hollow: {
        //             margin: 0,
        //             size: '70%',
        //             background: '#211a45',
        //             image: undefined,
        //             imageOffsetX: 0,
        //             imageOffsetY: 0,
        //             position: 'front',
        //             dropShadow: {
        //             enabled: true,
        //             top: 3,
        //             left: 0,
        //             blur: 4,
        //             opacity: 0.24
        //             }
        //         },
        //         track: {
        //             background: '#4e4e4e',
        //             strokeWidth: '67%',
        //             margin: 0, // margin is in pixels
        //             dropShadow: {
        //             enabled: true,
        //             top: -3,
        //             left: 0,
        //             blur: 4,
        //             opacity: 0.35
        //             }
        //         },
            
        //         dataLabels: {
        //             show: true,
        //             name: {
        //             offsetY: -10,
        //             show: true,
        //             color: '#2ee7a2',
        //             fontFamily: 'Roboto mono',
        //             fontSize: '17px'
        //             },
        //             value: {
        //             formatter: function(val) {
        //                 return parseInt(val);
        //             },
        //             color: '#2ee7a2',
        //             fontFamily: 'Roboto mono',
        //             fontSize: '36px',
        //             show: true,
        //             }
        //         }
        //         }
        //     },
        //     fill: {
        //         type: 'gradient',
        //         gradient: {
        //         shade: 'dark',
        //         type: 'horizontal',
        //         shadeIntensity: 0.5,
        //         gradientToColors: ['#fd894f'],
        //         inverseColors: true,
        //         opacityFrom: 1,
        //         opacityTo: 1,
        //         stops: [0, 100]
        //         }
        //     },
        //     stroke: {
        //         lineCap: 'round'
        //     },
        //     labels: ['Percent'],
        //     };
  
        // var chart_dashboard = new ApexCharts(document.querySelector("#chart__dashboard"), options);
        // chart_dashboard.render();

        // // history chart
        // var options = {
        //     series: [{
        //     name: 'Daily waterconsumption',
        //     data: [31, 40, 28, 51, 42, 109, 100],
        //   }],
        //     chart: {
        //     height: 350,
        //     foreColor: '#fff7ff',
        //     type: 'area',
        //     color: "#fff7ff",
        //     fontFamily: 'Roboto mono',
        //     toolbar: {
        //         show: false
        //     }
        //   },
        //   fill: {
        //     colors: "#fd894f"
        //   },
        //   markers: {
        //     colors: '#1d94ff'
        //  },
        //   dataLabels: {
        //     enabled: false,
        //   },
        //   stroke: {
        //     curve: 'smooth',
        //   },
        //   xaxis: {
        //     type: 'datetime',
        //     categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
        //   },
        //   tooltip: {
        //     x: {
        //         format: 'dd/MM/yy HH:mm'
        //     },
        //   },
        //   };
  
        // var chart_history = new ApexCharts(document.querySelector("#chart__history"), options);
        // chart_history.render();

        // Modal 
        const $modal = document.querySelector(".c-modal");
        const $button_open = document.querySelector(".c-modal__button--open");
        const $button_close = document.querySelector(".c-modal__button--submit");
        const $modal_shutdown = document.querySelector(".c-modal__shutdown");
        const $button_shutdown_open = document.querySelector(".c-modal__shutdown--open");
        const $button_shutdown_close = document.querySelector(".c-modal__shutdown--close");
        
        $button_open.addEventListener("click", () => {
            $modal.classList.toggle("c-show__modal");
        });

        $button_close.addEventListener("click", () => {
            $modal.classList.toggle("c-show__modal");
        });
        
        if ($button_shutdown_open) {
            $button_shutdown_open.addEventListener("click", () => {
                $modal_shutdown.classList.toggle("c-show__modal");
            });
        }

        if ($button_shutdown_close) {
            $button_shutdown_close.addEventListener("click", () => {
                $modal_shutdown.classList.toggle("c-show__modal");
            });
        }
        
        window.addEventListener("click", (e) => {
            if (e.target === $modal) {
                $modal.classList.toggle("c-show__modal");
            }

            if (e.target === $modal_shutdown) {
                $modal_shutdown.classList.toggle("c-show__modal");
            }
        });  
    };
    
    init();
}
