
select cliente.idcliente as comprador, cliente.nombre, cliente.direcci�n,
domicilio.coddomicilio, domicilio.fecha, domicilio.estado
from cliente inner join domicilio on cliente.idcliente = domicilio.coddomicilio
where domicilio.estado = 'devuelto'



