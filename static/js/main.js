function sidebarLeftToggle() {
  const sidebar = document.querySelector(".sidebar-left");
  sidebar.classList.toggle("show-sidebar-left");
}

function sidebarRightToggle() {
  const sidebar = document.querySelector(".sidebar-right");
  sidebar.classList.toggle("show-sidebar-right");
}

function initStyle(){
  document.addEventListener('DOMContentLoaded', (event) => {
    // style for code
    document.querySelectorAll('code').forEach((el) => {
      hljs.highlightElement(el);
    });
    hljs.initHighlightingOnLoad();

    // style for table
    document.querySelectorAll("table").forEach(items => {
      items.classList.add("table")
      items.classList.add("table-striped")
    })

    // add id to header
    const header = ["h1", "h2", "h3", "h4", "h5", "h6"]
    header.forEach(tag => {
      document.querySelectorAll(`.content ${tag}`).forEach(items => {
        const id = items.textContent.toLowerCase().replaceAll(" ", '-')
        items.setAttribute("id", id)
      })
    })

    document.querySelectorAll(".sidebar-right a").forEach(items => {
      items.setAttribute("href", `${window.location.href}${items.getAttribute("data_href")}`)
    })

    // set code language
    document.querySelectorAll("code").forEach(items => {
      const content = items.innerText.split("\n")[0]
      items.setAttribute("class","hljs")
      items.classList.add(`language-${content}`)
    })
  });
}