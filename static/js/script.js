async function createAutomaton() {
  const automatonType = document.getElementById("automaton-type").value;
  const automatonData = document.getElementById("automaton-data").value;  

  try {
      const response = await fetch(`/${automatonType}/create`, {  
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: automatonData  
      });

      if (response.ok) {
          const data = await response.json();
          
          alert(`O ID do autômato criado é: ${data.id}`);
      } else {
          const errorData = await response.json();
          alert(`Erro: ${errorData.detail}`);
      }
  } catch (error) {
      alert("Houve um erro ao criar o autômato.");
  }
}

async function acceptInput() {
  const automatonId = document.getElementById("automaton-id").value;
  const inputString = document.getElementById("input-string").value;

  try {
      const automatonType = document.getElementById("automaton-type").value;

      const response = await fetch(`/${automatonType}/${automatonId}/accept_input?input_string=${inputString}`, {  
          method: "POST"
      });

      const data = await response.json();
      if (data.message === "String aceita") {
          alert("String aceita!");
      } else {
          alert("String não aceita.");
      }
  } catch (error) {
      alert("Erro ao testar a string.");
  }
}

async function showDiagram() {
  const automatonId = document.getElementById("diagram-id").value;
  const automatonType = document.getElementById("diagram-type").value;

  if (automatonType !== "dfa" && automatonType !== "dpda") {
    alert("Somente os tipos DFA e DPDA são suportados para visualização de diagramas.");
    return;
  }

  try {
    const response = await fetch(`/${automatonType}/${automatonId}/show_diagram`);

    if (response.ok) {
      const imageBlob = await response.blob();
      const imageUrl = URL.createObjectURL(imageBlob);
      const diagramElement = document.getElementById("diagram");
      diagramElement.src = imageUrl;
      diagramElement.style.display = "block"; 
    } else {
      alert("Erro ao gerar o diagrama.");
    }
  } catch (error) {
    alert("Erro ao gerar o diagrama.");
  }
}

async function getAutomaton() {
  const automatonId = document.getElementById("automaton-id-get").value;
  const automatonType = document.getElementById("automaton-type-get").value;  

  try {
    const response = await fetch(`/${automatonType}/${automatonId}`, {
      method: "GET",
    });

    if (response.ok) {
      const data = await response.json();
      document.getElementById("automaton-display").textContent = JSON.stringify(data, null, 2);
      
    } else {
      const errorData = await response.json();
      alert(`Erro: ${errorData.detail}`);
    }
  } catch (error) {
    alert("Erro ao recuperar o autômato.");
  }
}