// getting all rows
document.querySelectorAll("#body_table tr").forEach(
// looping over each row and column 44
    function(row){
        let col = row.querySelector('td:nth-child(44)');
        col_text = col.textContent;
        // if case is solved
        if(col_text =='SOLVED'){
        // color green
            row.style.backgroundColor = '#426941' ;
            row.style.color = 'white';
        }
        // if action is pending
        else if(col_text == 'PENDING'){
        // color orange
            row.style.backgroundColor = '#b86111' ;
            row.style.color = 'white';
        }
        // others leave as is
        else{

        }

    }
)