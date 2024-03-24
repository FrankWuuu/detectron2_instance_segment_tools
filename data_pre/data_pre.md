

## without annotation
`tooth_ins/UESB_t/not_use` 285 \
`tooth_ins/UESB/train/images` 1500 \
`tooth_ins/children/all_imgs` 193 \
`tooth_ins/Panoramic_radiography_database/images` 598

`tufts/all_img` 1000

where `UESB_t` is modified by `UESB/test`
## with instance annotation 
`tooth_ins/UESB_t/train` 100 \
`tooth_ins/UESB_t/test` 93 

## Summary of Data Distribution in Number of Photos
```
| Dataset   | Number of Photos |
|-----------|------------------|
| Test      | 1000             |
| Train A   | 1000             |
| Train B   | 1000             |
| Train C   | 1000             |
```


```
|--tooth_ins
    |-- UESB_t
        |-- train
        |-- train
        |-- annotations
            |-- train.json
            |-- test.json
```