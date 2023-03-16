let follow_up_messages_btn = document.querySelector("#follow_up_messages_btn")
let foollo_up_template = `
<form action="/admin/message/check_message_id/" method="POST" dir="rtl">
    <p class="m-0 text-end">شماره پیگیری نامه را وارد کنید</p>
    <input type="text" name="message-id" placeholder="شماره پیگیری نامه" class="form-control" id="">
    <input type="hidden" name="csrf_token" value="${document.querySelector("#csrf_token").value}" id="">
    
    <button class="btn btn-success w-100 my-3">جستجو</button>
</form>

<div class="info my-5" dir="rtl">
    <h4 class="text-center">توجه فرمایید</h4>
    <ul class="d-flex flex-column justify-content-center align-items-center">
        <li>برای پیگیری نامه های سامانه باید کد پیگیری درج شده در سربرگ نامه هارا در کادر فوق وارد نمایید</li>
    </ul>
</div>
`
follow_up_messages_btn.addEventListener("click", (e) => {
    message_container.innerHTML = foollo_up_template
})