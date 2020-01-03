(() => {
    document.addEventListener('DOMContentLoaded', () => {
        const filterSettings = {
            from: 0,
            to: 0
        };
        const tableData = [];
        let adminRowData = '';
        document.querySelectorAll('.admin-row').forEach((element) => {
            adminRowData += element.outerHTML;
        });
        document.querySelectorAll('.table-row').forEach((element) => {
            tableData.push({
                date: new Date(element.querySelector('.date').innerText),
                dateNumber: new Date(element.querySelector('.date').innerText).getTime(),
                html: element.outerHTML
            });
        });

        function updateTableByDate() {
            const resultProductData = tableData.filter(function (element) {
                return (element.dateNumber > (filterSettings.from ? filterSettings.from : -99999999999999) && element.dateNumber < (filterSettings.to ? filterSettings.to : 99999999999999));
            });
            let newTableHtml = adminRowData;
            resultProductData.forEach((item) => {
                newTableHtml += item.html;
            });
            document.querySelector('.filtered-table tbody').innerHTML = newTableHtml;
        }

        document.querySelectorAll('.date-input').forEach((element) => {
            element.addEventListener('change', (e) => {
                if ( e.target.value ) {
                   filterSettings[e.target.getAttribute('data-filter')] = new Date(e.target.value).getTime();
                } else {
                    filterSettings[e.target.getAttribute('data-filter')] = 0;
                }

                updateTableByDate();
            });
        });
    });
})();