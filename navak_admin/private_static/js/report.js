async function getch_all_out_three_month() {
    let response = await fetch("/api/fetch/report/products/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        },
    })
    let data = await response.json()
    return data
}

async function getch_all_work_reports() {
    let response = await fetch("/api/_fetch/work/report/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        },
    })
    let data = await response.json()
    return data
}

async function set_up_chart() {
    let going_chart = document.querySelector("#out-store-chart")
    let out_store_data = await getch_all_out_three_month()

    const labels = out_store_data.dates;
    const data = {
        labels: labels,
        datasets: [
            {
                label: 'محصولات ورودی به انبار',
                data: out_store_data.in,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }, {
                label: 'محصولات خروجی از انبار',
                data: out_store_data.out,
                fill: false,
                borderColor: 'rgb(55, 200, 80)',
                tension: 0.1
            },
        ]
    };
    const config = {
        type: 'line',
        data: data,
    };

    let my_chart = document.querySelector("#out-store-chart")
    let crt = new Chart(
        my_chart,
        config
    )


    // work report chart set up
    let work_report_month_data = await getch_all_work_reports()
    const data_work_report = {
        labels:
        work_report_month_data.lables
        ,
        datasets: [{
            label: 'گزارش کار',
            data: work_report_month_data.datas,
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 1
        }],


    };

    const config_work_report = {
        type: 'doughnut',
        data: data_work_report,
    };
    let work_report_chart = document.querySelector("#work_report_sections")
    let report_work_crt = new Chart(
        work_report_chart,
        config_work_report
    )
    // end of work report chart set up


}

set_up_chart()