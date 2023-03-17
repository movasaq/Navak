// get projects type from server
// get get all projects that stoped by one month ago
// get get all projects that done in one month ago


async function fetch_grouth_of_projects() {
    let response = await fetch("/api/fetch/projects/grouth/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        }
    })

    let data = await response.json()
    return data
}

async function fech_all_projects_type() {
    let response = await fetch("/api/fetch/projects/type/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        }
    })

    let data = await response.json()
    return data
}

async function fech_all_projects_status() {
    let response = await fetch("/api/fetch/projects/all/status/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        }
    })

    let data = await response.json()
    return data
}


async function get_charts_data() {
    let data = await fetch_grouth_of_projects()
    let all_projects_status = document.querySelector("#all_projects_status")
    new Chart(all_projects_status, {
        type: 'pie',
        data: {
            labels: [
                'پایان یافته',
                'متوقف شده',
                'در حال انجام',
            ],
            datasets: [{
                label: '',
                data: [data.endded, data.stopped, data.doing],
                backgroundColor: [
                    'rgb(222, 196, 23)',
                    'rgb(222, 23, 23)',
                    ' rgb(23, 222, 76)',
                ],
                hoverOffset: 15
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });

    data = await fech_all_projects_type()
    let going_chart = document.querySelector("#going-projects-chart")
    new Chart(going_chart, {
        type: 'pie',
        data: {
            labels: [
                'تحقیقاتی',
                'تجاری',
                'نظامی',
            ],
            datasets: [{
                label: '',
                data: [data.dev, data.bues, data.mill],
                backgroundColor: [
                    'rgb(255, 99, 70)',
                    'rgb(54, 162, 50)',
                    'rgb(255, 205, 15)',
                ],
                hoverOffset: 15
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });
    // let grouth_projects = document.querySelector("#grouth-projects-chart")
    // new Chart(grouth_projects, {
    //     type: 'pie',
    //     data: {
    //         labels: [
    //         'تحقیقاتی',
    //         'تجاری',
    //         'نظامی',
    //         ],
    //         datasets: [{
    //         label: '',
    //         data: [300, 50, 100, 680,980,9874,1,2,54,87445,5],
    //         backgroundColor: [
    //             'rgb(255, 99, 132)',
    //             'rgb(54, 162, 235)',
    //             'rgb(255, 205, 86)',
    //         ],
    //         hoverOffset: 15
    //         }]
    //     },

    //     options: {
    //         responsive: true,
    //         maintainAspectRatio: false,
    //     }
    // });
}

get_charts_data()