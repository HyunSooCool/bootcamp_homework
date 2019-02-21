Sub test():

    For Each ws In Worksheets
        ws.Cells(1,9) = "Ticker"
        ws.Cells(1,10)= "Total Stock Volume"
    

    Dim current_ticker As String
    Dim next_ticker As String
    Dim vol As Double
    Dim last_low As Long
    Dim counter as long

    vol = 0
    last_low = ws.Cells(Rows.Count, 1).End(xlUp).Row
    counter = 2

        For i = 2 To last_low
            current_ticker = ws.Cells(i, 1).Value
            next_ticker = ws.Cells(i + 1, 1).Value

            If current_ticker = next_ticker Then
                vol = vol + ws.Cells(i, 7).Value
            
            ElseIf current_ticker <> next_ticker Then
                vol = vol + ws.Cells(i, 7).Value
                ws.Cells(counter, 9).Value = current_ticker
                ws.Cells(counter, 10).Value = vol
                counter = counter + 1
                vol = 0
            End If
        Next i
    Next ws

End Sub
