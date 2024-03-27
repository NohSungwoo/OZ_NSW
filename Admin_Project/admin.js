
const dataTable = document.getElementById('data-table')
const date = document.getElementById('date')
const checkAll = document.getElementById('checkAll')
const deleteBtn = document.getElementById('delete_btn')
const checkboxes = document.getElementsByClassName("form-check-input")

// 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
// 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리를 작성해 볼 수 있음
const data = [
    { category: "상의", brand: 'Supreme', gender: 'A', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', gender: 'F', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', gender: 'M', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', gender:'A', product: '빵빵이 키링', price: '29,000' },
    // ...
]
date.innerHTML = `${now()}` 
checkAll.addEventListener("click", selectAll) 
deleteBtn.addEventListener("click", deleteRow)        
     
    data.forEach((item) => {
        const row = dataTable.insertRow();
        row.insertCell(0).innerHTML = `<input class="form-check-input" type="checkbox">`
        row.insertCell(1).innerHTML = item.category;
        row.insertCell(2).innerHTML = item.brand;
        row.insertCell(3).innerHTML = item.gender;
        row.insertCell(4).innerHTML = item.product;
        row.insertCell(5).innerHTML = item.price;
    });
        
// 체크박스 모두 고르기
function selectAll(){
    if(document.getElementById("checkAll").checked==true){
        for(i=0; i<=data.length; i++){
            checkboxes[i].checked=true
        }
    }else{
        for(i=0; i<=data.length; i++){
            checkboxes[i].checked=false
        }
    }
}

// YYYY-MM-DD 함수
function now(){
    const today = new Date()
    const year = today.getFullYear()
    const month = (today.getMonth() + 1).toString().padStart(2, '0')
    const day = (today.getDate().toString().padStart(2, '0'))
    const date = `${year}-${month}-${day}`
    return date;
}     

function deleteRow(){
    let deleteData = [];
    for(i=0; i<checkboxes.length ; i++){
        if(checkboxes[i].checked==true){
            console.log(checkboxes[i])
            deleteData.push(checkboxes[i])
        }
    }
    deleteData.forEach((item) => {
        item.parentElement.parentElement.remove()
    })
}