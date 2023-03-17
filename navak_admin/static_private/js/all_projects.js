let rows = document.querySelectorAll(".table-row")
rows.forEach((each) => {
    each.style.cursor = "pointer"
    each.addEventListener("click", (e) => {
        window.location.href = "/admin/project/details/" + (e.currentTarget.dataset.target)
    })
})