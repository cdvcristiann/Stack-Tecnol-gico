new Vue({
    el: "#appNotas",    
    delimiters:['{$','$}'],
    data:{
        notas_txt: "",
        Estado:"",
        lista_notas: [],
        buscar_txt: "",
    },
    watch:{
        buscar_txt: function (val){
            this.buscaNotas(val);
        }
    },

    methods:{
        BuscarApi: function(buscar_txt){
            var self = this;
            axios.get("http://127.0.0.1:8000/Gestor/")
            .then(function(response){
                self.lista_notas = response.data
            })
        },

        eliminarNotasProcesos: function (notas_id) {            
            eliminar = confirm("Desea Eliminar la Nota")            
            if (eliminar==true) {          
                let index = this.lista_notas.findIndex(e => e.id=== notas_id);
                this.lista_notas.splice(index, 1) }
            },

        eliminarNotas: function (notas_id) {
                let index = this.lista_notas.findIndex(e => e.id=== notas_id);
                this.lista_notas.splice(index, 1) },            
        
        buscaNotas: function (valor) {
            this.lista_notas = this.lista_notas.filter((value) => {
                return value.notas.toLowerCase().indexOf(
                    valor.toLowerCase()
                )>=0
            }
          )
        },

        AgregarNotas: function(){
            var notas = {
                'id' : this.lista_notas.length,
                'notas' : this.notas_txt,
                'Estado' : this.Estado,
            };
            this.lista_notas.push(notas);
        },

        editarNotas: function(index){
            entrada= prompt("modifique la nota:")
            this.lista_notas[index].notas = entrada;
            estado = confirm("¿marcar como Terminado?")
            if (estado==true) {
                terminado="Terminado"
            this.lista_notas[index].Estado = terminado;}
            else{
              proceso="En proceso"
            this.lista_notas[index].Estado = proceso}
        }
        
        
        
        },
        
        
    
    })