import { useEffect, useState } from "react";
import "./Grafico.css";



function formatarMinutosESegundos(segundosTotais) {
    const minutos = Math.floor(segundosTotais / 60);
    const segundos = segundosTotais % 60;
  
    return `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
  }
  
  function formatarHorasEMinutos(segundosTotais) {
    const horas = Math.floor(segundosTotais / 3600);
    const minutos = Math.floor((segundosTotais % 3600) / 60);
  
    return `${horas.toString().padStart(2, '0')}:${minutos.toString().padStart(2, '0')}`;
  }

  function formatarTempoAuto(segundosTotais) {
    const horas = Math.floor(segundosTotais / 3600);
    const minutos = Math.floor((segundosTotais % 3600) / 60);
    const segundos = segundosTotais % 60;
  
    if (horas > 0) {
      return `${horas.toString().padStart(2, '0')}:${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
    } else if (minutos > 0) {
      return `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
    } else {
      return `${segundos.toString().padStart(2, '0')}s`;
    }
  }
  

function Grafico() {
  const [tempos, setTempos] = useState([140, 40, 60]);

  useEffect(() => {
    const interval = setInterval(() => {
      setTempos((prev) =>
        prev.map((valor) => (valor > 0 ? valor - 1 : 0))
      );
    }, 100);

    return () => clearInterval(interval);
  }, []);

  return (
    
    <div style={{
      backgroundColor: 'rgba(180, 166, 166, 0.05)',
      borderRadius: '20px',
      padding: '30px',
      boxShadow: '0 0 20px rgba(0, 255, 200, 0.2)'
    }}>
      <h2 className=".gradient-text">Visão geral do abastecimento: </h2>
      <div className="grafico">
  {tempos.map((tempo, i) => (
    <div key={i} className="barra-container">
      
      <div className="tempo-contador">{formatarTempoAuto(tempo)}</div>

      
      <div className="barra-wrapper">
        <div
          className="preenchimento"
          
          style={{
            height: `${tempo}%`,
            top: `${100 - tempo}%`,
            background: tempo > 50
              ? 'linear-gradient(to bottom,rgb(20, 219, 2),rgb(2, 250, 64))'
              : tempo > 20
              ? 'linear-gradient(to bottom,rgb(255, 123, 0),rgb(255, 157, 0))'
              : 'linear-gradient(to bottom,rgb(255, 4, 0),rgb(255, 4, 0))'
          }}
        />
      </div>

      <div className="nome-barra">
        {["Funil", "Conectores", "Esteira"][i]}
      </div>
    </div>
  ))}
</div>

    </div>
  );
}

export default Grafico;