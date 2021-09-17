SELECT Top (100) [id]
      ,[slaveId]
      ,[datStart]
      ,[datEnd]
      ,[duration]
      ,[channel1]
      ,[channel2]
      ,[channel3]
      ,[channel4]
      ,[error]
  INTO [WERMAWIN].[dbo].[datacopy]
  FROM [WERMAWIN].[dbo].[slaveData]
  

