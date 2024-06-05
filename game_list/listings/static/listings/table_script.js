let tb=document.getElementById("list_game");
let updown=[0,0,0]
let tbody=tb.querySelector('tbody')
let rowsarray = Array.from(tbody.rows)

tb.onclick = function(e) {
    if (e.target.tagName != 'TH') return;
    let th = e.target;
    sortGrid(th.cellIndex, updown[th.cellIndex]);
    st=th.innerHTML
    if (updown[th.cellIndex] == 1){
        st=st.slice(0,st.length-1) + '↓';
        th.innerHTML=st;
    }
    else{
        st=st.slice(0,st.length-1) + '↑';
        th.innerHTML=st;
    }
  };

function sortGrid(colNum, up_down) {
    let tbody = tb.querySelector('tbody');
    let rowsArray = Array.from(tbody.rows);
    let compare;
    switch (up_down) {
        
        case 0:
            compare = function(rowA, rowB) {
                return rowA.cells[colNum].innerText > rowB.cells[colNum].innerText ? 1 : -1;
            };

            updown[colNum] =1;
            break;

        case 1:
            compare = function(rowA, rowB) {
                return rowA.cells[colNum].innerText > rowB.cells[colNum].innerText ? -1 : 1;
            };

            updown[colNum] =0;  
            break;


    }
    rowsArray.sort(compare);

    tbody.append(...rowsArray);
}


function start() {
    let th=document.getElementById('prime')
    sortGrid(th.cellIndex, updown[th.cellIndex]);
    st=th.innerHTML
    if (updown[th.cellIndex] == 1){
        st=st.slice(0,st.length-1) + '↓';
        th.innerHTML=st;
    }
    else{
        st=st.slice(0,st.length-1) + '↑';
        th.innerHTML=st;
    }
}

window.onload = start()