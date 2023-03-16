let add_user = document.querySelector(".add-user")
let delete_user = document.querySelector(".delete-user")
let edit_user = document.querySelector(".edit-user")


function hidden_all_form() {
    let all_form = document.querySelectorAll("form")
    all_form.forEach((each) => {
        each.classList.add("d-none")
    })
}


function watch_user_type_employee() {
    let selectmenu = document.querySelector("#user-type")
    selectmenu.addEventListener("change", (e) => {
        console.log("GHjer")
        if (selectmenu[selectmenu.selectedIndex].innerHTML.trim() == "گروه کارمندان") {
            // show other option
            document.querySelector(".employee_option").innerHTML = `
                           
            <label for="first_name" class="w-100 my-2">
            <span>نام کارمند را وار نمایید</span>
            <input type="text" placeholder="نام کارمند" name="first_name" id="first_name" class="form-control" required>
        </label>
        <label for="last_name" class="w-100 my-2">
            <span>نام خانوادگی کارمند را وار نمایید</span>
            <input type="text" placeholder="نام خانوادگی کارمند" name="last_name" id="last_name" class="form-control" required>
        </label>
        <label for="birthday" class="w-100 my-2">
            <span>تاریخ تولد کارمند را وارد نمایید</span>
            <input type="text" placeholder="تاریخ تولد در فرمت 0000/00/00" name="birthday" id="birthday" class="form-control" required>
        </label>
        <label for="work_position" class="w-100 my-2">
            <span>موقعیت شعلی کارمند را وارد نمایید</span>
            <select class="form-select" id="work_position" name="work_position">
                <option value="تحقیق و توسعه">تحقیق و توسعه</option>
                <option value="حراست">حراست</option>
                <option value="حسابداری">حسابداری</option>
                <option value="تولید 1">تولید 1</option>
                <option value="تولید 2">تولید 2</option>
                <option value="سوله 700">سوله 700</option>
                <option value="مکانیک">مکانیک</option>
                <option value="مدیریت">مدیریت</option>
                <option value="اداری">اداری</option>
                <option value="بازرگانی">بازرگانی</option>
                <option value="کیفیت کنترل">کیفیت کنترل</option>
            </select>
        </label>
        <label for="meli_code" class="w-100 my-2">
            <span>کد ملی کارمند را وارد نمایید</span>
            <input type="text" placeholder="کد ملی کارمند" name="meli_code" id="meli_code" class="form-control" required>
        </label>


        <label for="birth_location" class="w-100 my-2">
            <span>محل تولد کارمند را وارد نمایید</span>
            <input type="text" placeholder="محل تولد" name="birth_location" id="birth_location" class="form-control" required>
        </label>
        <label for="phone" class="w-100 my-2">
            <span>تلفن کارمند را وارد نمایید</span>
            <input type="text" placeholder="تلفن کارمند" name="phone" id="phone" class="form-control" required>
        </label>
        <label for="emergency_tel" class="w-100 my-2">
            <span>تلفن موقعیت های ضروری کارمند را وارد نمایید</span>
            <input type="text" placeholder="تلفن موقعیت های ضروری کارمند" name="emergency_tel" id="emergency_tel" class="form-control" required>
        </label>
        <label for="address" class="w-100 my-2">
            <span>آدرس کارمند را وارد نمایید</span>
            <textarea placeholder="آدرس کارمند" name="address" id="address" class="form-control" required></textarea>
        </label>
        <label for="education" class="w-100 my-2">
            <span>مقطع تحصیلی کارمند را وارد نمایید</span>
            <input type="text" placeholder="مقطع تحصیلی کارمند" name="education" id="education" class="form-control" required>
        </label>
        <label for="staff_code" class="w-100 my-2">
            <span>کد کارمندی را وارد نمایید</span>
            <input type="text" placeholder="کد کارمندی " name="staff_code" id="staff_code" class="form-control" required>
        </label>
        <label for="contract_type" class="w-100 my-2">
            <span>نوع قرار داد کارمند را وارد نمایید</span>
            <input type="text" placeholder="نوع قرار داد " name="contract_type" id="contract_type" class="form-control" required>
        </label>
        <label for="start_contract" class="w-100 my-2">
            <span> تاریخ شروع قرارداد کارمند را وارد نمایید</span>
            <input type="text" placeholder="تاریخ شروع قرارداد در فرمت 0000/00/00" name="start_contract" id="start_contract" class="form-control" required>
        </label>
        <label for="end_contract" class="w-100 my-2">
            <span> تاریخ پایان قرارداد کارمند را وارد نمایید</span>
            <input type="text" placeholder=" تاریخ پایان قرارداد در فرمت 0000/00/00" name="end_contract" id="end_contract" class="form-control" required>
        </label>
        <label for="base_salary" class="w-100 my-2">
            <span>حقوق پایه کارمند  را وارد نمایید</span>
            <input type="text" placeholder=" حقوق کارمند" name="base_salary" id="base_salary" class="form-control" required>
        </label>


        `
        } else {
            // hidden other options
            document.querySelector(".employee_option").innerHTML = ``
        }
    })
}


add_user.addEventListener("click", (e) => {
    if (document.querySelector("#ADD-form").classList.contains("d-none")) {
        hidden_all_form()
        document.querySelector("#ADD-form").classList.remove("d-none")
        watch_user_type_employee()
    } else {
        document.querySelector("#ADD-form").classList.add("d-none")
    }
})

edit_user.addEventListener("click", (e) => {
    if (document.querySelector("#EDIT-form").classList.contains("d-none")) {
        hidden_all_form()
        document.querySelector("#EDIT-form").classList.remove("d-none")
    } else {
        document.querySelector("#EDIT-form").classList.add("d-none")
    }
})

delete_user.addEventListener("click", (e) => {
    if (document.querySelector("#DELETE-form").classList.contains("d-none")) {
        hidden_all_form()
        document.querySelector("#DELETE-form").classList.remove("d-none")
    } else {
        document.querySelector("#DELETE-form").classList.add("d-none")
    }
})



