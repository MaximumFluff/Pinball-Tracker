window.onload = () => {
  document.getElementById('search').addEventListener('input', filterTable);
}

const filterTable = () => {
  const searchValue = document.getElementById('search').value;
  const tableContents = document.getElementById('tableBody').children;
  for (item of Array.from(tableContents)) {
    if (!item.innerText.includes(searchValue)) {
      item.style.display = "none"
    }
    else {
      item.style.display = ""
    }
  }
}