// Replace 'YOUR_API_KEY' with your actual ChatGPT API key
const apiKey = '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';

// Function to send a request to ChatGPT API
async function sendRequest(prompt) {
  try {
    const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        prompt: prompt,
        max_tokens: 50, // Adjust max tokens as needed
      }),
    });

    if (response.ok) {
      const data = await response.json();
      return data.choices[0].text.trim();
    } else {
      throw new Error('ChatGPT API request failed');
    }
  } catch (error) {
    console.error('Error:', error);
    return 'Error processing request';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const textInput = document.getElementById('textInput');
  const responseTextarea = document.getElementById('response');
  const submitButton = document.querySelector('button[type="submit"]');

  submitButton.addEventListener('click', async () => {
    const inputText = textInput.value;

    if (inputText.trim() === '') {
      alert('Please enter text.');
      return;
    }

    submitButton.disabled = true;

    const responseText = await sendRequest(inputText);
    responseTextarea.value += `User: ${inputText}\nChatGPT: ${responseText}\n\n`;

    textInput.value = '';
    submitButton.disabled = false;
  });
});
