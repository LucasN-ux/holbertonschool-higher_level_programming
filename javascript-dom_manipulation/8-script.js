async function getdata() {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        const helloElement = document.querySelector('#hello');
        helloElement.textContent = result.hello;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
getdata();
