let counter_products = new Set()
let selected_products = new Set()


// read project products and show it to user 
let user_product_value = document.querySelector("#product-project")
if (user_product_value.value) {
    product_user_selected_value = JSON.parse(user_product_value.value)
    for (each in product_user_selected_value) {
        selected_products.add(product_user_selected_value[each])
    }
}
show_on_page_products()


let open_modal_products = document.querySelector(".open-modal-products")

open_modal_products.addEventListener("click", async (e) => {
    // get all products from db
    let products = await fetch_all_producs()

    add_products_to_modal(products)

    // open modal
    document.querySelector("#modal-products-trigger").click()

    // keep trak of what user selected
    user_select_products()

    show_on_page_products()

    let search_box = document.querySelector(".search-in-products-name")
    search_box.addEventListener("keydown", (e) => {
        //  if search box is empty show all
        if (e.target.value.trim() == "") {
            let products_name = document.querySelectorAll("p.p-name")
            products_name.forEach((e) => {
                if (e.parentElement.parentElement.classList.contains("d-none")) {
                    e.parentElement.parentElement.classList.remove("d-none")
                }
            })
        }
        if (e.target.value) {
            sort_products(e.target.value)
        }
    })
})


function sort_products(dt) {
    /// this function search in products for user
    let products_name = document.querySelectorAll("p.p-name")
    products_name.forEach((e) => {
        if (e.textContent.startsWith(dt)) {
            if (e.parentElement.parentElement.classList.contains("d-none")) {
                e.parentElement.parentElement.classList.remove("d-none")
            }
        } else {
            e.parentElement.parentElement.classList.add("d-none")
        }
    })
}

async function fetch_all_producs() {
    // this function get all products from db
    let response = await fetch("/api/admin/products/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        },
    })

    if (response.status == 200) {
        let data = await response.json()
        return data
    } else {
        return {}
    }
}


function add_products_to_modal(products) {
    // this function take products from api and put it in modal
    let container = document.querySelector("#products-containers")
    container.innerHTML = ""
    let counter = 0
    let checked_elem = []
    for (dt of products) {
        template = `
        <div class="col-12 d-flex flex-row-reverse justify-content-between align-items-center my-2 py-2 shadow-sm border rounded">
            <div class="d-flex flex-column justify-content-center align-items-center">
                <p class="m-0">خریداری شده از: ${dt.buy_form}</p>
                <p class="m-0">شرکت سازنده: ${dt.manufacture}</p>
            </div>
            <div class="d-flex justify-content-center align-items-center">
                <input type="checkbox"  id="product-${counter}" data-key="${dt.public_key}" class="form-check-input mx-2 pb-2 input-product">
                <p class="m-0 p-name">${dt.name}</p>
            </div>
        </div>
        `
        container.innerHTML += template

        // check elemnt just added to modal is selected by user before
        for (product of selected_products) {
            if (product.name == dt.name) {
                // add elemnt id to a list
                checked_elem.push("#" + "product-" + counter)
            }

        }
        counter++;
    }
    // set checked to true for element that have selected by user
    checked_elem.forEach((e) => {
        document.querySelector(e).checked = true
    })
}


function user_select_products() {
    let inputs = document.querySelectorAll(".input-product")
    inputs.forEach((each) => {
        each.addEventListener("click", (e) => {
            // get user selected product name and key
            let temp = {}
            temp["name"] = e.target.parentElement.children[1].textContent
            temp["key"] = e.target.dataset.key
            temp["total"] = 1
            temp["gets"] = 0

            container = temp
            // if user select a product from store keep watching
            if (e.target.checked) {
                selected_products.add(container)
            } else {
                // if user unselected a product find it from object and delete it
                for (obj of selected_products) {
                    if (obj.name == temp["name"]) {
                        selected_products.delete(obj)
                        return
                    }
                }

            }

        })
    })

}


function show_on_page_products() {
    //this function show user selected prducts in page
    let container = document.querySelector(".product-contaoner-pice")
    container.innerHTML = ""
    for (p of selected_products) {
        let tr = document.createElement("tr")
        let td1 = document.createElement("td")
        let td2 = document.createElement("td")
        let input = document.createElement("input")
        input.type = "number"
        td1.textContent = p.name
        input.value = p.total
        input.setAttribute("data-key", p.key)
        tr.appendChild(td1)
        tr.appendChild(td2)
        td2.appendChild(input)
        container.appendChild(tr)

        // add event for when use want change product numbers
        input.addEventListener("keyup", (e) => {
            let key = (e.target.dataset.key)
            for (each of selected_products) {
                if (each.key == key) {
                    if (!e.target.value || e.target.value == 0) {
                        e.target.value = 1
                        each.total == e.target.value
                        return
                    }
                    if (each.total == e.target.value) {
                        return
                    }
                    if (selected_products.delete((each))) {
                        each.total = e.target.value
                        selected_products.add((each))
                    }
                }
            }
        })
    }
    document.querySelector("#modal-products-store").addEventListener("hide.bs.modal", (e) => {
        let container = document.querySelector(".product-contaoner-pice")
        container.innerHTML = ""
        for (p of selected_products) {
            let tr = document.createElement("tr")
            let td1 = document.createElement("td")
            let td2 = document.createElement("td")
            let input = document.createElement("input")
            input.type = "number"
            td1.textContent = p.name
            input.value = p.total
            input.setAttribute("data-key", p.key)
            tr.appendChild(td1)
            tr.appendChild(td2)
            td2.appendChild(input)
            container.appendChild(tr)

            // add event for when use want change product numbers
            input.addEventListener("keyup", (e) => {
                let key = (e.target.dataset.key)
                for (each of selected_products) {
                    if (each.key == key) {
                        if (!e.target.value || e.target.value == 0) {
                            e.target.value = 1
                            each.total = e.target.value
                            return
                        }
                        if (each.total == e.target.value) {
                            return
                        }
                        if (selected_products.delete((each))) {
                            each.total = e.target.value
                            selected_products.add((each))
                        }
                    }
                }
            })
        }
    })

}


function register_poject() {
    // this function wach when form submiting replace fake value with actuall value and submit form to server
    let form = document.querySelector("#form-register-project")
    form.addEventListener("submit", (e) => {
        if (selected_products.size == 0) {
            document.querySelector("#product-project").value = "{}"
        } else {
            res = {...Array.from(selected_products)}
            document.querySelector("#product-project").value = JSON.stringify(res)
        }
    })

}


register_poject()