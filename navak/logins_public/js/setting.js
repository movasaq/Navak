document.querySelectorAll(".referrer").forEach((each) => {
    each.value = window.location.href
})

async function bring_user_data() {
    // this function bring user data
    let response = await fetch("/api/user/data/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        }
    })
    let data = await response.json()
    if (response.status == 200) {
        return data
    } else {
        return false
    }

}

async function put_user_info() {
    let user_data = await bring_user_data()
    if (user_data) {
        let user_tag = document.querySelector("#user_tag")
        let user_group = document.querySelector("#group-user")
        let username = document.querySelector("#username-user")
        user_tag.textContent = "@" + user_data.data.user_tag
        username.textContent = user_data.data.username
        user_group.textContent = user_data.data.group
    }
}

put_user_info()