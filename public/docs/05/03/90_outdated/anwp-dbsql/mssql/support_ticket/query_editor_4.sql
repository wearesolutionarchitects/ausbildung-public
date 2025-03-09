DECLARE @RC int
DECLARE @editor_id int

--TODO: Hier Parameterwerte festlegen.

EXECUTE @RC = [dbo].[spGetTicketsByUserId] 
   @editor_id = 4
   select 'Bearbeiter' = @RC
GO