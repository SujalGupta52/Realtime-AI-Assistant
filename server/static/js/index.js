"use strict";
function makeCunksOfText(text) {
  const maxLength = 190;
  let speechChunks = [];

  // Split the text into chunks of maximum length maxLength without breaking words
  while (text.length > 0) {
    if (text.length <= maxLength) {
      speechChunks.push(text);
      break;
    }

    let chunk = text.substring(0, maxLength + 1);

    let lastSpaceIndex = chunk.lastIndexOf(" ");
    if (lastSpaceIndex !== -1) {
      speechChunks.push(text.substring(0, lastSpaceIndex));
      text = text.substring(lastSpaceIndex + 1);
    } else {
      // If there are no spaces in the chunk, split at the maxLength
      speechChunks.push(text.substring(0, maxLength));
      text = text.substring(maxLength);
    }
  }

  return speechChunks;
}

async function speakText(text) {
  const speechChunks = makeCunksOfText(text);
  for (let i = 0; i < speechChunks.length; i++) {
    await new Promise((resolve, reject) => {
      window.speechSynthesis.cancel();
      let speech = new SpeechSynthesisUtterance(speechChunks[i]);
      speech.rate = 1;
      speech.lang = "hi-IN";
      window.speechSynthesis.speak(speech);
      speech.onend = () => {
        resolve();
      };
      speech.onerror = (error) => {
        resolve();
      };
    });
  }
}

async function say(text) {
  await speakText(text);
}

let log = console.log.bind(console),
  stream,
  recorder,
  counter = 1,
  chunks,
  alreadyKeyDown = false,
  media,
  speechIndicator = document.querySelector(".speak-indicator"),
  answerContainer = document.querySelector(".answer");

window.onload = (e) => {
  media = {
    tag: "audio",
    type: "audio/wav",
    ext: ".wav",
    gUM: { audio: true },
  };
  navigator.mediaDevices
    .getUserMedia(media.gUM)
    .then((_stream) => {
      stream = _stream;
      recorder = new MediaRecorder(stream);
      recorder.ondataavailable = (e) => {
        chunks.push(e.data);
        if (recorder.state == "inactive") makeLink();
      };
    })
    .catch(log);
};

window.onkeydown = (e) => {
  window.speechSynthesis.cancel();
  if (e.code === "Space" && !alreadyKeyDown) {
    speechIndicator.classList.toggle("speaking");
    alreadyKeyDown = true;
    chunks = [];
    recorder.start();
  }
};

window.onkeyup = (e) => {
  speechIndicator.classList.toggle("speaking");
  alreadyKeyDown = false;
  recorder.stop();
};

async function makeLink() {
  let blob = new Blob(chunks, { type: media.type });
  const file = new File([blob], `${counter++}${media.ext}`, {
    type: media.type,
  });
  const formData = new FormData();
  formData.append("file", file);

  const options = {
    method: "POST",
    body: formData,
  };
  try {
    const res = await fetch("/", options);
    const answer = await res.text();
    answerContainer.textContent = answer;
    say(answer);
  } catch (e) {
    log(e);
  }
  // const audio = document.getElementById("myAudio");
  // audio.src = `/generated/${file_path[file_path.length - 1]}`;
  // audio.play();
}

setInterval(function () {
  if (window.speechSynthesis.speaking) {
    speechIndicator.classList.add("ai");
  }
}, 100);

setInterval(function () {
  if (!window.speechSynthesis.speaking) {
    speechIndicator.classList.remove("ai");
  }
}, 100);
