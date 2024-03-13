
function convertToSha() {
    const inputField = document.getElementById("input-text");
    const sha1Elem = document.getElementById("sha1");
    const sha256Elem = document.getElementById("sha256");
    const sha384Elem = document.getElementById("sha384");
    const sha512Elem = document.getElementById("sha512");

    digestMessage(inputField.value, "SHA-1").then((digestHex) => sha1Elem.value = digestHex);
    digestMessage(inputField.value, "SHA-256").then((digestHex) => sha256Elem.value = digestHex);
    digestMessage(inputField.value, "SHA-384").then((digestHex) => sha384Elem.value = digestHex);
    digestMessage(inputField.value, "SHA-512").then((digestHex) => sha512Elem.value = digestHex);
}


async function digestMessage(message, algorithm) {
    if (!message) {
        return "";
    }

    const msgUint8 = new TextEncoder().encode(message); // encode as (utf-8) Uint8Array
    const hashBuffer = await crypto.subtle.digest(algorithm, msgUint8); // hash the message
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // convert buffer to byte array
    const hashHex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join(""); // convert bytes to hex string
    return hashHex;
}
