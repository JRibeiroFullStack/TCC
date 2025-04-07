import Navbar from "../componentes/Navbar/Navbar"
import Graficos from "../componentes/Grafico/Grafico"
import './MonitoramentoPagina.css'

function MonitoramentoPagina(){
    return(
        <div className="espacamento-grafico">
            <Navbar />
        <div className='Graficos'>
          <Graficos />
        </div>
    </div>
    )
}

export default MonitoramentoPagina