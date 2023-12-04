function deleteNote(note) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ note: note }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }