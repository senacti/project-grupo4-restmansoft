create proc agregarprod
@codproducto as int,
@cantidad as int
as
update producto set cantidad=cantidad+@cantidad
where codproducto=@codproducto

select*from producto

exec agregarprod 1,1

