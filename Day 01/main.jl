function main()
    open("./Day 01/input.txt") do f
        L = []
        cur_sum = 0
        for line in readlines(f)
            if line == ""
                push!(L, cur_sum)
                cur_sum = 0
            else
                cur_sum += parse(Int64, line)
            end
        end

        sorted_L = sort(L, rev = true)

        println("Highest is $(sorted_L[1])")
        println("Sum of 3 highest is $(sorted_L[1] + sorted_L[2] + sorted_L[3])")
    end
end
