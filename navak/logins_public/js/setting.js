async function bring_user_data() {
    // this function bring user data
    let response = await fetch("/setting/_user/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("#csrf_token").value
        }
    })
    if (response.status == 200) {
        let data = await response.json()
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
    } else {
        window.alert("خطایی رخ داد دوباره امتحان کنید")
    }
}

put_user_info()